"""
Full End-to-End System Test
Tests the complete brand agent workflow for a coffee shop
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END
from state import BrandState

# Import Agents
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent
from agents.design_agent import design_agent
from agents.deliverables_agent import deliverables_agent

def create_test_workflow():
    """Creates a workflow without interrupts for testing"""
    workflow = StateGraph(BrandState)
    
    # Add nodes
    workflow.add_node("research", research_agent)
    workflow.add_node("strategy", strategy_agent)
    workflow.add_node("design_identity", design_agent)
    workflow.add_node("deliverables", deliverables_agent)
    
    # Add edges (no interrupts)
    workflow.set_entry_point("research")
    workflow.add_edge("research", "strategy")
    workflow.add_edge("strategy", "design_identity")
    workflow.add_edge("design_identity", "deliverables")
    workflow.add_edge("deliverables", END)
    
    return workflow.compile()

def test_full_workflow():
    """Test complete brand strategy generation workflow"""
    print("=" * 70)
    print("🚀 BRAND AGENT - FULL SYSTEM TEST")
    print("=" * 70)
    print()
    
    # Sample client brief for GreenBean Cafe
    client_brief = {
        "company_name": "GreenBean Cafe",
        "business_type": "Sustainable Coffee Shop",
        "target_audience": "Environmentally conscious millennials and Gen Z",
        "industry": "coffee shop",
        "brand_type": "new",
        "budget_tier": "premium",
        "core_values": ["sustainability", "community", "quality"],
        "mission_statement": "Serving exceptional coffee while protecting our planet"
    }
    
    print("📋 Client Brief:")
    print(f"   Company: {client_brief['company_name']}")
    print(f"   Industry: {client_brief['industry']}")
    print(f"   Target: {client_brief['target_audience']}")
    print(f"   Core Values: {', '.join(client_brief['core_values'])}")
    print()
    
    # Build the test graph (without interrupts)
    print("🔧 Building orchestrator graph...")
    graph = create_test_workflow()
    print("   ✅ Graph built successfully")
    print()
    
    # Initialize state
    initial_state = {
        "messages": [],
        "client_brief": client_brief,
        "research_outputs": None,
        "strategy_outputs": None,
        "design_outputs": None,
        "deliverables": None,
        "approval_status": {
            "research_approved": True,  # Auto-approve for testing
            "strategy_approved": True,  # Auto-approve for testing
            "design_approved": True
        },
        "next_step": "",
        "errors": []
    }
    
    config = {"configurable": {"thread_id": "test_run_001"}}
    
    print("▶️  Running complete workflow...\n")
    print("-" * 70)
    
    try:
        # Run the graph
        result = None
        step_count = 0
        
        for output in graph.stream(initial_state, config=config):
            step_count += 1
            node_name = list(output.keys())[0] if output else "unknown"
            print(f"\n🔄 Step {step_count}: {node_name.upper()}")
            
            if node_name == "research":
                print("   📊 Conducting market research...")
            elif node_name == "strategy":
                print("   🎯 Defining brand strategy...")
            elif node_name == "design_identity":
                print("   🎨 Creating visual identity...")
            elif node_name == "deliverables":
                print("   📦 Compiling deliverables...")
                
            result = output
        
        print()
        print("-" * 70)
        print()
        
        if result:
            final_state = result[list(result.keys())[-1]]
            
            print("=" * 70)
            print("✅ WORKFLOW COMPLETED SUCCESSFULLY")
            print("=" * 70)
            print()
            
            # Display results
            if "research_outputs" in final_state and final_state["research_outputs"]:
                print("📊 RESEARCH RESULTS:")
                research = final_state["research_outputs"]
                if "market_analysis" in research:
                    print(f"   Market Analysis: {str(research['market_analysis'])[:100]}...")
                if "competitor_map" in research:
                    print(f"   Competitors: {str(research['competitor_map'])[:100]}...")
                print()
            
            if "strategy_outputs" in final_state and final_state["strategy_outputs"]:
                print("🎯 STRATEGY RESULTS:")
                strategy = final_state["strategy_outputs"]
                if "positioning" in strategy:
                    print(f"   Positioning: {strategy['positioning']}")
                if "personality" in strategy:
                    print(f"   Personality: {strategy['personality']}")
                if "messaging_framework" in strategy:
                    print(f"   Framework: {str(strategy['messaging_framework'])[:100]}...")
                print()
            
            if "design_outputs" in final_state and final_state["design_outputs"]:
                print("🎨 DESIGN RESULTS:")
                design = final_state["design_outputs"]
                if "color_palette" in design:
                    print(f"   Color Palette: {design['color_palette']}")
                if "typography" in design:
                    print(f"   Typography: {str(design['typography'])[:100]}...")
                if "logo_concepts" in design:
                    print(f"   Logo Concepts: {str(design['logo_concepts'])[:100]}...")
                print()
            
            if "deliverable_outputs" in final_state and final_state["deliverable_outputs"]:
                print("📦 DELIVERABLES:")
                deliverables = final_state["deliverable_outputs"]
                for key, value in deliverables.items():
                    print(f"   {key}: {value}")
                print()
            
            print("=" * 70)
            print("🎉 All systems operational!")
            print("=" * 70)
            return True
        else:
            print("❌ Workflow failed - no result returned")
            return False
            
    except Exception as e:
        print()
        print("-" * 70)
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        print("-" * 70)
        return False

if __name__ == '__main__':
    success = test_full_workflow()
    sys.exit(0 if success else 1)
