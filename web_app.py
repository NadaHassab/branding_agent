"""
Flask web application for Brand Agent System
Provides a user-friendly interface for running brand strategy workflows
"""
from flask import Flask, render_template, request, jsonify, session, send_file
import os
import sys
import json
from datetime import datetime
import threading
import uuid

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import BrandState, ClientBrief
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent
from agents.design_agent import design_agent
from agents.deliverables_agent import deliverables_agent

app = Flask(__name__)
app.secret_key = 'brand_agent_secret_key_2026'

# Store workflow states in memory (in production, use Redis or database)
workflow_states = {}
workflow_apps = {}

def should_continue_after_strategy(state: BrandState):
    """Check if strategy is approved before continuing to design."""
    if state["approval_status"]["strategy_approved"]:
        return "design_identity"
    else:
        return "strategy"

def create_workflow():
    """Creates the LangGraph workflow with interrupts."""
    memory = MemorySaver()
    workflow = StateGraph(BrandState)
    
    workflow.add_node("research", research_agent)
    workflow.add_node("strategy", strategy_agent)
    workflow.add_node("design_identity", design_agent)
    workflow.add_node("deliverables", deliverables_agent)
    
    workflow.set_entry_point("research")
    workflow.add_edge("research", "strategy")
    workflow.add_conditional_edges(
        "strategy",
        should_continue_after_strategy,
        {
            "design_identity": "design_identity",
            "strategy": "strategy"
        }
    )
    workflow.add_edge("design_identity", "deliverables")
    workflow.add_edge("deliverables", END)
    
    return workflow.compile(
        checkpointer=memory,
        interrupt_before=["strategy", "design_identity"]
    )

def run_workflow_async(workflow_id, initial_state, config):
    """Run workflow in background thread."""
    try:
        app_instance = workflow_apps[workflow_id]
        
        # Start workflow
        workflow_states[workflow_id]['status'] = 'running'
        workflow_states[workflow_id]['current_step'] = 'research'
        
        for event in app_instance.stream(initial_state, config):
            for node_name, node_output in event.items():
                workflow_states[workflow_id]['current_step'] = node_name
                workflow_states[workflow_id]['completed_steps'].append(node_name)
                
                if node_name == "research":
                    workflow_states[workflow_id]['status'] = 'research_complete'
                    workflow_states[workflow_id]['research_outputs'] = node_output.get('research_outputs')
                    
                elif node_name == "strategy":
                    workflow_states[workflow_id]['status'] = 'awaiting_approval'
                    workflow_states[workflow_id]['strategy_outputs'] = node_output.get('strategy_outputs')
                    # Pause here - waiting for approval
                    return
                    
                elif node_name == "design_identity":
                    workflow_states[workflow_id]['status'] = 'design_complete'
                    workflow_states[workflow_id]['design_outputs'] = node_output.get('design_outputs')
                    
                elif node_name == "deliverables":
                    workflow_states[workflow_id]['status'] = 'completed'
                    workflow_states[workflow_id]['deliverables'] = node_output.get('deliverables')
        
        # Get final state
        final_state = app_instance.get_state(config)
        workflow_states[workflow_id]['final_state'] = final_state.values
        
    except Exception as e:
        workflow_states[workflow_id]['status'] = 'error'
        workflow_states[workflow_id]['error'] = str(e)

@app.route('/')
def index():
    """Main page with brief submission form."""
    return render_template('index.html')

@app.route('/start_workflow', methods=['POST'])
def start_workflow():
    """Start a new brand strategy workflow."""
    try:
        data = request.json
        
        # Create client brief from form data
        client_brief = ClientBrief(
            company_name=data.get('company_name', ''),
            industry=data.get('industry', ''),
            target_audience=data.get('target_audience', ''),
            brand_type=data.get('brand_type', 'new'),
            budget_tier=data.get('budget_tier', 'premium'),
            core_values=data.get('core_values', '').split(','),
            mission_statement=data.get('mission_statement', '')
        )
        
        # Create initial state
        initial_state = BrandState(
            messages=[],
            client_brief=client_brief,
            research_outputs=None,
            strategy_outputs=None,
            design_outputs=None,
            deliverables=None,
            approval_status={
                "research_approved": False,
                "strategy_approved": False,
                "design_approved": False
            },
            next_step="research",
            errors=[]
        )
        
        # Generate workflow ID
        workflow_id = str(uuid.uuid4())
        config = {"configurable": {"thread_id": workflow_id}}
        
        # Create workflow instance
        workflow_apps[workflow_id] = create_workflow()
        
        # Initialize workflow state tracking
        workflow_states[workflow_id] = {
            'id': workflow_id,
            'status': 'initialized',
            'current_step': None,
            'completed_steps': [],
            'client_brief': client_brief,
            'created_at': datetime.now().isoformat(),
            'research_outputs': None,
            'strategy_outputs': None,
            'design_outputs': None,
            'deliverables': None,
            'error': None
        }
        
        # Start workflow in background thread
        thread = threading.Thread(
            target=run_workflow_async,
            args=(workflow_id, initial_state, config)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'workflow_id': workflow_id,
            'message': 'Workflow started successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/workflow_status/<workflow_id>')
def workflow_status(workflow_id):
    """Get current status of a workflow."""
    if workflow_id not in workflow_states:
        return jsonify({'error': 'Workflow not found'}), 404
    
    state = workflow_states[workflow_id]
    return jsonify(state)

@app.route('/approve_strategy/<workflow_id>', methods=['POST'])
def approve_strategy(workflow_id):
    """Approve strategy and continue to design phase."""
    try:
        if workflow_id not in workflow_apps:
            return jsonify({'error': 'Workflow not found'}), 404
        
        app_instance = workflow_apps[workflow_id]
        config = {"configurable": {"thread_id": workflow_id}}
        
        # Get current state
        current_state = app_instance.get_state(config)
        
        # Approve strategy
        current_state.values["approval_status"]["strategy_approved"] = True
        app_instance.update_state(config, current_state.values)
        
        # Continue workflow in background
        workflow_states[workflow_id]['status'] = 'continuing'
        thread = threading.Thread(
            target=run_workflow_async,
            args=(workflow_id, None, config)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Strategy approved, continuing to design phase'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/workflow/<workflow_id>')
def workflow_page(workflow_id):
    """Workflow progress page."""
    if workflow_id not in workflow_states:
        return "Workflow not found", 404
    
    return render_template('workflow.html', workflow_id=workflow_id)

@app.route('/download/<workflow_id>/<file_type>')
def download_file(workflow_id, file_type):
    """Download generated deliverables."""
    if workflow_id not in workflow_states:
        return "Workflow not found", 404
    
    state = workflow_states[workflow_id]
    if not state.get('deliverables'):
        return "Deliverables not ready", 404
    
    deliverables = state['deliverables']
    
    if file_type == 'strategy':
        file_path = deliverables.get('strategy_doc')
    elif file_type == 'guidelines':
        file_path = deliverables.get('brand_guidelines')
    else:
        return "Invalid file type", 400
    
    if not file_path or not os.path.exists(file_path):
        return "File not found", 404
    
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    print("🚀 Starting Brand Agent Web Application...")
    print("📱 Open your browser to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
