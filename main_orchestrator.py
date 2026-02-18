import sys
import os

# Add the project root to the python path so we can import modules easily
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from typing import List, Literal
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import BrandState, ClientBrief

# Import Agents
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent
from agents.design_agent import design_agent
from agents.deliverables_agent import deliverables_agent

def should_continue_after_strategy(state: BrandState) -> Literal["design_identity", "strategy"]:
    """
    Conditional edge: Check if strategy is approved before continuing to design.
    If not approved, loop back to strategy for refinement.
    """
    if state["approval_status"]["strategy_approved"]:
        return "design_identity"
    else:
        print("⏸️  [INTERRUPT] Strategy requires human approval before proceeding to design.")
        return "strategy"

def create_workflow():
    """
    Constructs the LangGraph workflow for the Brand Agent with human-in-the-loop interrupts.
    """
    # Add checkpointer for state persistence and interrupts
    memory = MemorySaver()
    workflow = StateGraph(BrandState)

    # 1. Add Nodes (Agents)
    workflow.add_node("research", research_agent)
    workflow.add_node("strategy", strategy_agent)
    workflow.add_node("design_identity", design_agent)
    workflow.add_node("deliverables", deliverables_agent)

    # 2. Add Edges with Interrupts
    # Start -> Research
    workflow.set_entry_point("research")
    
    # Research -> Strategy (with interrupt after research for review)
    workflow.add_edge("research", "strategy")
    
    # Strategy -> Design (CONDITIONAL - requires human approval)
    # This creates an interrupt point where human can review strategy before design starts
    workflow.add_conditional_edges(
        "strategy",
        should_continue_after_strategy,
        {
            "design_identity": "design_identity",
            "strategy": "strategy"  # Loop back if not approved
        }
    )
    
    # Design -> Deliverables
    workflow.add_edge("design_identity", "deliverables")
    
    # Deliverables -> End
    workflow.add_edge("deliverables", END)

    # Compile with checkpointer to enable interrupts
    return workflow.compile(
        checkpointer=memory,
        interrupt_before=["strategy", "design_identity"]  # Pause before strategy and design for human review
    )

if __name__ == "__main__":
    print("🚀 Starting Brand Agent Orchestrator with Human-in-the-Loop...")
    
    # Example Client Brief
    initial_brief: ClientBrief = {
        "company_name": "EcoFresh",
        "industry": "Food Delivery",
        "target_audience": "Urban millennials, eco-conscious",
        "brand_type": "new",
        "budget_tier": "premium",
        "core_values": ["Sustainability", "Transparency", "Local"],
        "mission_statement": "To make sustainable eating accessible to everyone."
    }
    
    initial_state = BrandState(
        messages=[],
        client_brief=initial_brief,
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
    
    app = create_workflow()
    
    print(f"📋 Processing brief for: {initial_brief['company_name']}")
    
    # Configuration for the run
    config = {"configurable": {"thread_id": "brand_agent_session_1"}}
    
    # Run with interrupts - this will pause at interrupt points
    print("\n🔄 Running workflow with interrupt points for human review...")
    print("   Interrupts are set before: strategy, design_identity")
    print("   To continue after interrupt, approve the strategy in the state and resume.\n")
    
    # Stream events to see progress
    for event in app.stream(initial_state, config):
        for node_name, node_output in event.items():
            print(f"\n✅ Completed: {node_name}")
            if node_name == "research":
                print("   📊 Research insights ready for review")
            elif node_name == "strategy":
                print("   🧠 Strategy ready for approval")
                print("   ⏸️  INTERRUPT: Review strategy before proceeding to design")
                print("\n   To approve and continue:")
                print("   1. Review strategy_outputs in the state")
                print("   2. Set approval_status['strategy_approved'] = True")
                print("   3. Call app.invoke(None, config) to resume")
                
                # For demo purposes, auto-approve here
                # In production, this would wait for human input
                print("\n   [AUTO-APPROVING FOR DEMO]")
                current_state = app.get_state(config)
                current_state.values["approval_status"]["strategy_approved"] = True
                app.update_state(config, current_state.values)
                
            elif node_name == "design_identity":
                print("   🎨 Design concepts generated")
    
    # Get final result
    final_state = app.get_state(config)
    
    print("\n✅ Workflow Completed!")
    print("\n--- Final Deliverables ---")
    if final_state.values.get("deliverables"):
        print(f"Strategy Doc: {final_state.values['deliverables'].get('strategy_doc')}")
        print(f"Guidelines: {final_state.values['deliverables'].get('brand_guidelines')}")
    else:
        print("❌ No deliverables generated (check errors).")
        if final_state.values.get("errors"):
            print(f"Errors: {final_state.values['errors']}")
