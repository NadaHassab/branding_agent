"""
Test the comprehensive brand agent system with skincare app brief.
This will generate complete professional brand guidelines following PDF structure.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from state import BrandState
from skincare_brief import SKINCARE_APP_BRIEF
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent
from agents.design_agent import design_agent
from agents.deliverables_agent import deliverables_agent
import json

if __name__ == "__main__":
    print("=" * 80)
    print("[TEST] COMPREHENSIVE BRAND GUIDELINES SYSTEM")
    print("[APP] AI Skincare Advisor App")
    print("[TARGET] Females 18-35, scientific-based personalized skincare")
    print("[COMPETITORS] lovi.care, skinsyncapp.ai, getskinbliss.com")
    print("[USP] 100% UNBIASED - No brand affiliations, customer-first only")
    print("=" * 80)
    print()
    
    print("CLIENT BRIEF:")
    print(f"   Company: {SKINCARE_APP_BRIEF['company_name']}")
    print(f"   Industry: {SKINCARE_APP_BRIEF['industry']}")
    print(f"   Target: {SKINCARE_APP_BRIEF['target_audience']}")
    print(f"   Mission: {SKINCARE_APP_BRIEF['mission_statement'][:100]}...")
    print(f"   USP: {SKINCARE_APP_BRIEF['unique_value_proposition'][:120]}...")
    print()
    print("   Brand Differentiators:")
    for diff in SKINCARE_APP_BRIEF['brand_differentiators']:
        print(f"      * {diff}")
    print()
    print("=" * 80)
    print()
    
    # Initialize state
    initial_state = BrandState(
        messages=[],
        client_brief=SKINCARE_APP_BRIEF,
        research_outputs=None,
        strategy_outputs=None,
        design_outputs=None,
        deliverables=None,
        approval_status={
            "research_approved": True,  # Auto-approve for testing
            "strategy_approved": True,  # Auto-approve for testing
            "design_approved": True     # Auto-approve for testing
        },
        next_step="research",
        errors=[]
    )
    
    try:
        # Step 1: Research Agent
        print("[STEP 1] RUNNING RESEARCH AGENT...")
        print("-" * 80)
        state_after_research = research_agent(initial_state)
        print("[OK] Research completed!")
        print()
        
        # Step 2: Strategy Agent
        print("[STEP 2] RUNNING STRATEGY AGENT...")
        print("-" * 80)
        state_after_strategy = strategy_agent(state_after_research)
        print("[OK] Strategy completed!")
        print()
        
        # Step 3: Design Agent (with comprehensive tools)
        print("[STEP 3] RUNNING COMPREHENSIVE DESIGN AGENT...")
        print("-" * 80)
        state_after_design = design_agent(state_after_strategy)
        print("[OK] Design completed!")
        print()
        
        # Step 4: Deliverables Agent (with comprehensive guidelines)
        print("[STEP 4] RUNNING DELIVERABLES AGENT...")
        print("-" * 80)
        final_state = deliverables_agent(state_after_design)
        print("[OK] Deliverables completed!")
        print()
    
        print("=" * 80)
        print("[SUCCESS] PIPELINE COMPLETE!")
        print("=" * 80)
        print()
        
        # Display summary
        print("DELIVERABLES SUMMARY:")
        print("-" * 80)
        
        deliverables = final_state.get("deliverables", {})
        
        print(f"[DOC] Strategy Document: {deliverables.get('strategy_doc', 'N/A')}")
        print(f"[DOC] Brand Guidelines: {deliverables.get('brand_guidelines', 'N/A')}")
        print()
        
        asset_summary = deliverables.get("asset_summary", {})
        print(f"[VISUAL ASSETS]")
        print(f"   Logo Variations: {asset_summary.get('total_logo_variations', 0)}")
        print(f"   - Primary Logo (Horizontal)")
        print(f"   - Primary Logo (Stacked)")
        print(f"   - Wordmark Only")
        print(f"   - Icon Only")
        print(f"   - Square Format")
        print(f"   - Construction Guide")
        print()
        print(f"   Brand Applications: {asset_summary.get('total_applications', 0)}")
        print(f"   - Business Card")
        print(f"   - Letterhead (A4)")
        print(f"   - Envelope (DL)")
        print(f"   - App Icon")
        print(f"   - Notepad")
        print()
        print(f"   Color Palette:")
        print(f"   - Primary Colors: {asset_summary.get('primary_colors', 0)}")
        print(f"   - Secondary Colors: {asset_summary.get('secondary_colors', 0)}")
        print()
        
        # Display design details
        design_outputs = final_state.get("design_outputs", {})
        
        if "design_direction" in design_outputs:
            print("[DESIGN DIRECTION]")
            direction = design_outputs["design_direction"]
            print(f"   Wordmark: {direction.get('wordmark_direction', 'N/A')[:100]}...")
            print(f"   Icon: {direction.get('icon_direction', 'N/A')[:100]}...")
            print(f"   Mood: {direction.get('mood_board', 'N/A')}")
            print()
        
        if "typography" in design_outputs:
            print("[TYPOGRAPHY]")
            typo = design_outputs["typography"]
            print(f"   Primary Font: {typo.get('primary_font', 'N/A')}")
            print(f"   Secondary Font: {typo.get('secondary_font', 'N/A')}")
            print()
        
        if "color_palette" in design_outputs:
            print("[COLOR PALETTE]")
            palette = design_outputs["color_palette"]
            
            primary = palette.get("primary_colors", {})
            print(f"   Primary Colors:")
            for name, hex_code in primary.items():
                print(f"      {name}: {hex_code}")
            
            secondary = palette.get("secondary_colors", {})
            print(f"   Secondary Colors:")
            for name, hex_code in secondary.items():
                print(f"      {name}: {hex_code}")
            print()
        
        if "logo_system" in design_outputs:
            print("[LOGO SYSTEM - Poyo.ai Task IDs]")
            logos = design_outputs["logo_system"]
            for logo_name, logo_data in logos.items():
                task_id = logo_data.get("task_id", "N/A")
                print(f"   {logo_name.replace('_', ' ').title()}: {task_id}")
            print()
        
        if "applications" in design_outputs:
            print("[BRAND APPLICATIONS - Poyo.ai Task IDs]")
            apps = design_outputs["applications"]
            for app_name, app_data in apps.items():
                task_id = app_data.get("task_id", "N/A")
                print(f"   {app_name.replace('_', ' ').title()}: {task_id}")
            print()
        
        print("=" * 80)
        print("[SUCCESS] TEST COMPLETE - Check output/ folder for deliverables")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
