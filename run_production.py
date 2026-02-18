"""
PRODUCTION BRAND GUIDELINES GENERATOR
"""
from state import BrandState
from agents.research_agent import research_agent
from agents.strategy_agent import strategy_agent
from agents.design_agent import design_agent
from agents.deliverables_agent import deliverables_agent
from client_brief import CLIENT_BRIEF
import json
import os
from datetime import datetime

def run_production_brand_system():
    """
    Production-ready brand guidelines generator
    Generates complete professional brand guidelines following CEEM PDF structure:
    
    Structure:
    1. Cover Page
    2. Welcome / Introduction    
    3. Table of Contents
    4. Section 01 - Overview (About, Mission/Vision/Purpose)
    5. Section 02 - The Logo
       - Logo Lockup (Wordmark + Icon)
       - Logo Construction (Grid, proportions)
       - Logo Variations (Linear/Stacked)
       - Color Variations
       - Clearspace (25mm/10mm print, 160px/75px digital)
       - Placement (Left/Right/Center)
       - Co-branding Rules
       - Incorrect Usage
    6. Section 03 - Colors
       - Primary Colors (RGB, HEX, CMYK)
       - Secondary Colors (Palettes)
    7. Section 04 - Typography
       - Primary Font
       - Secondary Font
       - Typeface Rules / Hierarchy
    8. Section 05 - Pattern (if applicable)
    9. Applications (Business Card, Letterhead, Envelope, etc.)
    """
    
    print("=" * 100)
    print(" " * 25 + "PRODUCTION BRAND GUIDELINES GENERATOR")
    print("=" * 100)
    print()
    
    print(f"[CLIENT] {CLIENT_BRIEF.get('company_name', 'Client')} - {CLIENT_BRIEF.get('industry', '')}")
    print(f"[AUDIENCE] {CLIENT_BRIEF.get('target_audience', 'N/A')}")
    print("[OUTPUT] Professional Brand Guidelines Document (DOCX)")
    print()
    print("=" * 100)
    print()
    
    # Initialize state with production settings
    initial_state = BrandState(
        messages=[],
        client_brief=CLIENT_BRIEF,
        research_outputs=None,
        strategy_outputs=None,
        design_outputs=None,
        deliverables=None,
        approval_status={
            "research_approved": True,   # Production mode: auto-approve
            "strategy_approved": True,   # Production mode: auto-approve
            "design_approved": True      # Production mode: auto-approve
        },
        next_step="research",
        errors=[]
    )
    
    try:
        # STEP 1: RESEARCH
        print("[1/4] RESEARCH AGENT - Market Analysis & Competitor Research")
        print("-" * 100)
        state_after_research = research_agent(initial_state)
        print("[COMPLETE] Research phase finished")
        print()
        
        # STEP 2: STRATEGY
        print("[2/4] STRATEGY AGENT - Brand Positioning & Messaging")
        print("-" * 100)
        state_after_strategy = strategy_agent(state_after_research)
        
        if state_after_strategy.get('strategy_outputs'):
            strategy = state_after_strategy['strategy_outputs']
            print(f"[POSITIONING] {strategy.get('positioning', 'N/A')[:150]}...")
            print(f"[PERSONALITY] {', '.join(strategy.get('personality', [])[:6])}")
            if 'name_options' in strategy:
                print(f"[BRAND NAMES] {', '.join(strategy.get('name_options', [])[:5])}")
        print("[COMPLETE] Strategy phase finished")
        print()
        
        # STEP 3: DESIGN (COMPREHENSIVE)
        print("[3/4] DESIGN AGENT - Complete Visual Identity System")
        print("-" * 100)
        print("Generating:")
        print("  - Logo System (6 variations: Horizontal, Stacked, Wordmark, Icon, Square, Construction)")
        print("  - Color Palette (Primary + Secondary with HEX/RGB/CMYK)")
        print("  - Typography (Hierarchy, Font families, Rules)")
        print("  - Grid System (12-column, 8pt baseline)")
        print("  - Brand Applications (Business card, Letterhead, Envelope, App icon, Notepad)")
        print()
        
        state_after_design = design_agent(state_after_strategy)
        
        design_outputs = state_after_design.get('design_outputs', {})
        print()
        print("[DESIGN COMPLETE]")
        print(f"  Logo Variations: {len(design_outputs.get('logo_system', {}))} types")
        print(f"  Color Palette: {len(design_outputs.get('color_palette', {}).get('primary_colors', {}))} primary + {len(design_outputs.get('color_palette', {}).get('secondary_colors', {}))} secondary")
        print(f"  Typography: {design_outputs.get('typography', {}).get('primary_font', 'N/A')} + {design_outputs.get('typography', {}).get('secondary_font', 'N/A')}")
        print(f"  Applications: {len(design_outputs.get('applications', {}))} mockups")
        print(f"  Grid System: {design_outputs.get('grid_system', 'N/A')}")
        print("[COMPLETE] Design phase finished")
        print()
        
        # STEP 4: DELIVERABLES
        print("[4/4] DELIVERABLES AGENT - Professional Documents")
        print("-" * 100)
        print("Creating:")
        print("  1. Brand Strategy Document (Strategy, Positioning, Messaging)")
        print("  2. Comprehensive Brand Guidelines (Following CEEM PDF Structure)")
        print("     - Cover & Welcome")
        print("     - Table of Contents")
        print("     - Overview (About, Mission/Vision/Purpose)")
        print("     - Logo System (All variations, Construction, Clearspace, Rules)")
        print("     - Color System (Primary/Secondary with codes)")
        print("     - Typography (Fonts, Hierarchy, Rules)")
        print("     - Pattern/Grid System")
        print("     - Applications (Stationery, Digital)")
        print()
        
        final_state = deliverables_agent(state_after_design)
        print("[COMPLETE] Deliverables phase finished")
        print()
        
        # PRODUCTION SUMMARY
        print("=" * 100)
        print(" " * 35 + "PRODUCTION COMPLETE!")
        print("=" * 100)
        print()
        
        deliverables = final_state.get("deliverables", {})
        
        print("[OUTPUT FILES]")
        print(f"  1. {deliverables.get('strategy_doc', 'N/A')}")
        print(f"  2. {deliverables.get('brand_guidelines', 'N/A')}")
        print()
        
        asset_summary = deliverables.get("asset_summary", {})
        print("[ASSETS GENERATED]")
        print(f"  Logo Variations: {asset_summary.get('total_logo_variations', 0)}")
        print(f"    - Primary Logo (Horizontal & Stacked)")
        print(f"    - Wordmark Only")
        print(f"    - Icon Only")
        print(f"    - Square Format (Social media/App)")
        print(f"    - Construction Guide (Grid & Measurements)")
        print()
        print(f"  Color Palette: {asset_summary.get('primary_colors', 0)} primary + {asset_summary.get('secondary_colors', 0)} secondary")
        print()
        print(f"  Brand Applications: {asset_summary.get('total_applications', 0)}")
        print(f"    - Business Card (3.5 x 2 inches)")
        print(f"    - Letterhead (A4 / 210mm x 297mm)")
        print(f"    - Envelope (DL / 110mm x 220mm)")
        print(f"    - App Icon (iOS/Android)")
        print(f"    - Notepad (A6)")
        print()
        
        # Show generated colors
        color_palette = deliverables.get("color_palette", {})
        if color_palette:
            print("[COLOR PALETTE]")
            print("  Primary Colors:")
            for name, hex_code in color_palette.get("primary_colors", {}).items():
                print(f"    {name.replace('_', ' ').title():20} {hex_code}")
            
            print("\n  Secondary Colors:")
            for name, hex_code in color_palette.get("secondary_colors", {}).items():
                print(f"    {name.replace('_', ' ').title():20} {hex_code}")
            print()
        
        # Show typography
        typography = deliverables.get("typography", {})
        if typography:
            print("[TYPOGRAPHY SYSTEM]")
            print(f"  Primary Font:   {typography.get('primary_font', 'N/A')}")
            print(f"  Secondary Font: {typography.get('secondary_font', 'N/A')}")
            print()
        
        # Brand direction summary
        design_direction = design_outputs.get("design_direction", {})
        if design_direction:
            print("[BRAND IDENTITY DIRECTION]")
            print(f"  Wordmark: {design_direction.get('wordmark_direction', 'N/A')[:80]}...")
            print(f"  Icon:     {design_direction.get('icon_direction', 'N/A')[:80]}...")
            print(f"  Mood:     {design_direction.get('mood_board', 'N/A')[:80]}...")
            print()
        
        # Poyo.ai task info (rate limited, but structure is ready)
        logo_system = design_outputs.get("logo_system", {})
        if logo_system:
            has_tasks = any(logo.get("task_id") for logo in logo_system.values())
            if has_tasks:
                print("[POYO.AI GENERATION STATUS]")
                for logo_name, logo_data in logo_system.items():
                    task_id = logo_data.get("task_id", "Rate Limited")
                    print(f"  {logo_name.replace('_', ' ').title():30} Task: {task_id}")
                print()
        
        print("=" * 100)
        print("[SUCCESS] Professional brand guidelines generated successfully!")
        print("[LOCATION] Check output/ folder for DOCX files")
        print("=" * 100)
        
        return final_state
        
    except Exception as e:
        print()
        print("[ERROR] Production pipeline failed")
        print(f"[DETAILS] {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nProduction Run Started: {timestamp}\n")
    
    result = run_production_brand_system()
    
    if result:
        print(f"\nProduction Run Complete: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n[NEXT STEPS]")
        print("  1. Review output/Brand_Strategy.docx")
        print("  2. Review output/Comprehensive_Brand_Guidelines.docx")
        print("  3. If Poyo.ai tasks generated, check status at: https://api.poyo.ai/task/<task_id>")
        print("  4. Download generated logo/application images when ready")
        print("  5. Customize guidelines document with actual branding visuals")
    else:
        print("\n[FAILED] Production run encountered errors. Check logs above.")
