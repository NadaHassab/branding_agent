from state import BrandState
from tools.document_tools import create_brand_strategy_document
from tools.comprehensive_guidelines import create_comprehensive_brand_guidelines
import os

def deliverables_agent(state: BrandState) -> BrandState:
    """
    Agent responsible for compiling and generating comprehensive final deliverables.
    Creates professional brand guidelines following PDF structure:
    - Logo system (wordmark, icon, construction, variations)
    - Color system (primary, secondary, usage rules)
    - Typography (hierarchy, rules, font families)
    - Grid system and spacing
    - Brand applications (business cards, letterhead, envelope, app icons, etc.)
    - Usage guidelines (dos and don'ts)
    """
    print("[DELIVERABLES AGENT] Packaging comprehensive brand identity system...")
    
    strategy = state["strategy_outputs"]
    design = state["design_outputs"]
    
    # 1. Create Strategy Document
    strategy_doc_path = os.path.join("output", "Brand_Strategy.docx")
    create_brand_strategy_document.invoke({
        "strategy_content": strategy,
        "output_path": strategy_doc_path
    })
    print(f"   ✅ Strategy document: {strategy_doc_path}")
    
    # 2. Create Comprehensive Brand Guidelines Document (following PDF structure)
    guidelines_path = os.path.join("output", "Comprehensive_Brand_Guidelines.docx")
    create_comprehensive_brand_guidelines.invoke({
        "strategy": strategy,
        "design": design.get("design_direction", {}),  # full design direction schema
        "logo_system": design.get("logo_system", {}),  # 6 logo variations
        "applications": design.get("applications", {}),  # business card, letterhead, envelope, app icon, notepad
        "output_path": guidelines_path
    })
    print(f"   ✅ Comprehensive guidelines: {guidelines_path}")
    
    print(f"\n✅ DELIVERABLES COMPLETE:")
    print(f"   📄 Strategy Document: {strategy_doc_path}")
    print(f"   📘 Brand Guidelines: {guidelines_path}")
    print(f"   🎨 Logo System: {len(design.get('logo_system', {}))} variations")
    print(f"   🎨 Color Palette: {len(design.get('color_palette', {}).get('primary_colors', {}))} primary + {len(design.get('color_palette', {}).get('secondary_colors', {}))} secondary colors")
    print(f"   🎨 Applications: {len(design.get('applications', {}))} mockups")

    return {
        **state,
        "deliverables": {
            "strategy_doc": strategy_doc_path,
            "brand_guidelines": guidelines_path,
            "logo_system": design.get("logo_system", {}),
            "applications": design.get("applications", {}),
            "color_palette": design.get("color_palette", {}),
            "typography": design.get("typography", {}),
            "asset_summary": {
                "total_logo_variations": len(design.get("logo_system", {})),
                "total_applications": len(design.get("applications", {})),
                "primary_colors": len(design.get("color_palette", {}).get("primary_colors", {})),
                "secondary_colors": len(design.get("color_palette", {}).get("secondary_colors", {}))
            }
        }
    }
