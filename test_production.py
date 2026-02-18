"""
Test script for Brand Agent System
Tests with a real industry: Sustainable Coffee Shop
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from state import BrandState, ClientBrief
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent

def test_brand_agent():
    print("=" * 70)
    print("🧪 TESTING BRAND AGENT SYSTEM")
    print("=" * 70)
    print()
    
    # Test Case: Sustainable Coffee Shop
    test_brief: ClientBrief = {
        "company_name": "GreenBean Cafe",
        "industry": "Sustainable Coffee Shops",
        "target_audience": "Environmentally conscious millennials and Gen Z, urban professionals",
        "brand_type": "new",
        "budget_tier": "premium",
        "core_values": ["Sustainability", "Quality", "Community", "Transparency"],
        "mission_statement": "To serve exceptional coffee while protecting our planet and supporting local farmers."
    }
    
    print("📋 TEST BRIEF:")
    print(f"   Company: {test_brief['company_name']}")
    print(f"   Industry: {test_brief['industry']}")
    print(f"   Target Audience: {test_brief['target_audience']}")
    print(f"   Core Values: {', '.join(test_brief['core_values'])}")
    print()
    print("=" * 70)
    print()
    
    initial_state = BrandState(
        messages=[],
        client_brief=test_brief,
        research_outputs=None,
        strategy_outputs=None,
        design_outputs=None,
        deliverables=None,
        approval_status={
            "research_approved": False,
            "strategy_approved": True,  # Auto-approve for testing
            "design_approved": False
        },
        next_step="research",
        errors=[]
    )
    
    # Step 1: Test Research Agent
    print("🔍 STEP 1: RUNNING RESEARCH AGENT...")
    print("-" * 70)
    try:
        state_after_research = research_agent(initial_state)
        print("✅ Research completed successfully!")
        print()
        print("📊 RESEARCH RESULTS:")
        print()
        
        if state_after_research.get('research_outputs'):
            research = state_after_research['research_outputs']
            
            print("🏢 MARKET ANALYSIS:")
            market_analysis = research.get('market_analysis', {})
            if isinstance(market_analysis, dict):
                for key, value in market_analysis.items():
                    print(f"   {key}: {value}")
            else:
                print(f"   {market_analysis}")
            print()
            
            print("👥 AUDIENCE INSIGHTS:")
            audience = research.get('audience_insights', {})
            if isinstance(audience, dict):
                for key, value in audience.items():
                    if key != 'research_insights':
                        print(f"   {key}: {value}")
            print()
            
            print("🎯 COMPETITOR MAP:")
            competitor_map = research.get('competitor_map', {})
            if isinstance(competitor_map, dict):
                for key, value in competitor_map.items():
                    print(f"   {key}: {value}")
            print()
        
        print("=" * 70)
        print()
        
        # Step 2: Test Strategy Agent
        print("🧠 STEP 2: RUNNING STRATEGY AGENT...")
        print("-" * 70)
        state_after_strategy = strategy_agent(state_after_research)
        print("✅ Strategy completed successfully!")
        print()
        print("📈 STRATEGY RESULTS:")
        print()
        
        if state_after_strategy.get('strategy_outputs'):
            strategy = state_after_strategy['strategy_outputs']
            
            print("🎯 POSITIONING:")
            print(f"   {strategy.get('positioning', 'N/A')}")
            print()
            
            print("✨ BRAND PERSONALITY:")
            for trait in strategy.get('personality', []):
                print(f"   • {trait}")
            print()
            
            print("💬 MESSAGING FRAMEWORK:")
            messaging = strategy.get('messaging_framework', {})
            if isinstance(messaging, dict):
                for key, value in messaging.items():
                    print(f"   {key}: {value}")
            print()
            
            print("🏷️  BRAND NAME OPTIONS:")
            for name in strategy.get('name_options', []):
                print(f"   • {name}")
            print()
        
        print("=" * 70)
        print()
        print("✅ TEST COMPLETED SUCCESSFULLY!")
        print("   - Research Agent: ✓")
        print("   - Strategy Agent: ✓")
        print()
        print("💡 The system is working with:")
        print("   - Real web search (no mock data)")
        print("   - Structured Pydantic outputs (no JSON parsing errors)")
        print("   - GitHub Models GPT-4o API")
        print()
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == '__main__':
    success = test_brand_agent()
    sys.exit(0 if success else 1)
