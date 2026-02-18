from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from state import BrandState
from tools.comprehensive_design_tools import (
    generate_comprehensive_logo_system,
    generate_brand_applications,
    generate_scientific_color_palette
)
from schemas import DesignDirectionSchema
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, LLM_TEMPERATURE_DESIGN, REQUEST_TIMEOUT, LLM_PROVIDER
import json

# Initialize LLM - Supports both GitHub Models and OpenAI
llm = ChatOpenAI(
    model=LLM_MODEL,  # gpt-4o
    temperature=LLM_TEMPERATURE_DESIGN,  # 0.7 for creative design
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
    timeout=REQUEST_TIMEOUT,  # 120 seconds
    max_retries=3
)
print(f"[DESIGN AGENT] Using LLM provider: {LLM_PROVIDER}")

def design_agent(state: BrandState) -> BrandState:
    """
    Agent responsible for creating comprehensive visual identity following professional brand guidelines structure.
    Generates: Logo system (6 variations), color palette (primary/secondary), typography, applications, grid system.
    """
    print("[DESIGN AGENT] Creating comprehensive visual identity...")
    
    strategy = state["strategy_outputs"]
    brief = state["client_brief"]
    
    # Extract company/brand name from strategy or brief
    company_name = strategy.get("name_options", [brief.get("company_name", "Brand")])[0] if "name_options" in strategy else brief.get("company_name", "Brand")
    industry = brief.get("industry", "Technology")
    
    # 1. Determine comprehensive design direction using LLM with expanded schema
    design_brief_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert Creative Director specializing in comprehensive brand identity systems.
        Create detailed visual direction including:
        - Wordmark design direction (typeface style, letterform treatment, custom modifications)
        - Icon/symbol design direction (geometric shapes, metaphors, abstract/literal approach)
        - Combined logo composition and layout
        - Primary color palette (3-4 colors with HEX codes for brand core)
        - Secondary color palette (3-5 colors with HEX codes for accents and variety)
        - Typography system (primary font for headings/UI, secondary font for body)
        - Grid system (12-column, 8pt baseline, etc.)
        - Overall design rationale and mood board keywords
        """),
        ("user", """Strategy: {strategy}
        
        Brief: {brief}
        
        Generate your response in valid JSON format with this exact structure:
        {{
          "wordmark_direction": "Detailed direction for the wordmark/typography logo (e.g., 'Modern sans-serif, clean geometric letterforms, slightly rounded corners for warmth, all lowercase for approachability')",
          "icon_direction": "Detailed direction for the icon/symbol (e.g., 'Abstract molecular structure representing scientific precision, hexagonal core shape symbolizing stability, gradient treatment for innovation')",
          "combined_logo_direction": "How wordmark and icon work together (e.g., 'Icon positioned left of wordmark, aligned to cap height, total lockup maintains 3:1 horizontal ratio')",
          "primary_colors_hex": ["#HEXCODE1", "#HEXCODE2", "#HEXCODE3"],
          "secondary_colors_hex": ["#HEXCODE1", "#HEXCODE2", "#HEXCODE3", "#HEXCODE4"],
          "primary_font_family": "Font name for headings/UI (e.g., 'Inter', 'Montserrat', 'Poppins')",
          "secondary_font_family": "Font name for body copy (e.g., 'Open Sans', 'Lato', 'Source Sans')",
          "grid_system": "Layout grid specification (e.g., '12-column grid with 8pt baseline grid, 16px gutters')",
          "design_keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
          "mood_board": "Visual mood/aesthetic (e.g., 'Clean minimalism meets scientific precision, soft gradients, medical-grade trustworthiness')",
          "design_rationale": "Comprehensive explanation of all design choices and how they support brand strategy"
        }}
        
        Output only valid JSON, no markdown, no code blocks, no other text.
        """)
    ])
    
    # Use LLM without response_format to avoid parse() call
    chain = design_brief_prompt | llm
    
    response = chain.invoke({
        "strategy": json.dumps(strategy),
        "brief": json.dumps(brief)
    })
    
    # Parse and validate the JSON response
    try:
        design_dict = json.loads(response.content)
        design_directives = DesignDirectionSchema(**design_dict)
    except (json.JSONDecodeError, Exception) as e:
        print(f"   ⚠️ JSON parsing failed, using fallback: {e}")
        # Fallback with expanded schema
        design_directives = DesignDirectionSchema(
            wordmark_direction="Modern sans-serif wordmark with clean letterforms",
            icon_direction="Abstract geometric icon representing innovation",
            combined_logo_direction="Icon left, wordmark right, balanced composition",
            primary_colors_hex=["#0066CC", "#FFFFFF", "#1A1A1A"],
            secondary_colors_hex=["#00AAFF", "#66D9FF", "#003D7A", "#E6F5FF"],
            primary_font_family="Inter",
            secondary_font_family="Open Sans",
            grid_system="12-column grid with 8pt baseline grid",
            design_keywords=["modern", "professional", "innovative", "trustworthy", "clean"],
            mood_board="Contemporary minimalism with technological sophistication",
            design_rationale="Design system reflects modern professionalism and innovation while maintaining approachability"
        )
    
    print(f"   ✅ Design direction established: {design_directives.mood_board}")

    # 2. Generate Comprehensive Logo System (6 variations)
    print(f"   🎨 Generating comprehensive logo system for {company_name}...")
    logo_system = generate_comprehensive_logo_system.invoke({
        "brand_direction": {
            "company_name": company_name,
            "industry": industry,
            "wordmark_direction": design_directives.wordmark_direction,
            "icon_direction": design_directives.icon_direction,
            "mood": design_directives.mood_board,
            "colors": design_directives.primary_colors_hex
        }
    })
    print(f"   ✅ Logo system generated: {len(logo_system)} variations")
    
    # 3. Generate Scientific Color Palette (structured with meanings and usage rules)
    print(f"   🎨 Creating scientific color palette...")
    color_palette = generate_scientific_color_palette.invoke({
        "primary_colors_hex": design_directives.primary_colors_hex,
        "secondary_colors_hex": design_directives.secondary_colors_hex,
        "mood": design_directives.mood_board
    })
    print(f"   ✅ Color palette: {len(color_palette.get('primary_colors', {}))} primary, {len(color_palette.get('secondary_colors', {}))} secondary")
    
    # 4. Generate Brand Applications (5+ mockups: business card, letterhead, envelope, app icon, notepad)
    print(f"   🎨 Generating brand application mockups...")
    applications = generate_brand_applications.invoke({
        "brand_info": {
            "company_name": company_name,
            "primary_colors_hex": design_directives.primary_colors_hex,
            "industry": industry,
            "logo_description": design_directives.combined_logo_direction
        }
    })
    print(f"   ✅ Applications generated: {len(applications)} mockups")
    
    # 5. Define Typography Hierarchy (detailed specification)
    typography = {
        "primary_font": design_directives.primary_font_family,
        "secondary_font": design_directives.secondary_font_family,
        "hierarchy": {
            "h1_display": f"{design_directives.primary_font_family}, 48pt/3rem, Bold",
            "h2_heading": f"{design_directives.primary_font_family}, 36pt/2.25rem, Semibold",
            "h3_subheading": f"{design_directives.primary_font_family}, 24pt/1.5rem, Medium",
            "body": f"{design_directives.secondary_font_family}, 16pt/1rem, Regular",
            "small": f"{design_directives.secondary_font_family}, 14pt/0.875rem, Regular",
            "caption": f"{design_directives.secondary_font_family}, 12pt/0.75rem, Regular"
        },
        "rules": [
            "Never use more than 2 font families in one design",
            "Maintain 1.5x line height for body text readability",
            "Use font weight to establish hierarchy, not size alone",
            "Ensure WCAG AA contrast ratios (4.5:1 minimum for body text)"
        ]
    }

    return {
        **state,
        "design_outputs": {
            "logo_system": logo_system,  # 6 variations: horizontal, stacked, wordmark, icon, square, construction
            "color_palette": color_palette,  # primary + secondary colors with meanings and usage rules
            "typography": typography,  # complete hierarchy and rules
            "applications": applications,  # business card, letterhead, envelope, app icon, notepad
            "grid_system": design_directives.grid_system,
            "design_direction": design_directives.dict(),  # full direction for guidelines document
            "design_rationale": design_directives.design_rationale
        },
        "approval_status": {**state["approval_status"], "design_approved": True}
    }
