"""
Comprehensive Brand Guidelines Generator
Creates complete brand identity following professional brand guidelines structure:
- Logo (Wordmark, Icon, Construction, Variations)
- Colors (Primary, Secondary, Usage)
- Typography (Hierarchy, Usage Rules)
- Grid System
- Applications (Business Cards, Stationery, Digital)
"""
from langchain_core.tools import tool
from typing import List, Dict
import requests
from config import POYO_API_KEY, POYO_API_ENDPOINT, POYO_MODEL, POYO_DEFAULT_SIZE, POYO_DEFAULT_RESOLUTION

@tool
def generate_comprehensive_logo_system(brand_direction: Dict) -> Dict:
    """
    Generates a complete logo system with multiple variations using Poyo.ai Nano Banana Pro.
    
    Creates:
    - Primary Logo (Wordmark + Icon combined)
    - Wordmark Only (text-based logo)
    - Icon/Symbol Only (standalone mark)
    - Horizontal Layout
    - Stacked Layout
    - Color on White variations
    - White on Color variations
    - Monochrome (Black)
    - Monochrome (White)
    
    Args:
        brand_direction: Dictionary with:
            - company_name: Brand name
            - wordmark_direction: Creative direction for wordmark
            - icon_direction: Creative direction for icon
            - industry: Industry/category
            - mood: Visual mood description
            - colors: Primary brand colors
    
    Returns:
        Dictionary with task IDs for all logo variations
    """
    print("🎨 [COMPREHENSIVE LOGO SYSTEM] Generating complete logo system...")
    print(f"   Brand: {brand_direction.get('company_name', 'Unknown')}")
    print(f"   Model: {POYO_MODEL}")
    
    company_name = brand_direction.get('company_name', 'Brand')
    industry = brand_direction.get('industry', 'Technology')
    wordmark_dir = brand_direction.get('wordmark_direction', 'Modern san-serif wordmark')
    icon_dir = brand_direction.get('icon_direction', 'Abstract icon')
    mood = brand_direction.get('mood', 'Professional')
    
    logo_variations = {}
    
    # Define all logo variations to generate
    variations = [
        {
            "name": "primary_logo_horizontal",
            "prompt": f"Professional brand logo for {company_name}, {industry} company. {wordmark_dir} combined with {icon_dir}. Horizontal layout with icon on left and wordmark on right. {mood} aesthetic. Vector art style, clean lines, white background, ultra high quality, professional branding, corporate identity, minimalist design"
        },
        {
            "name": "primary_logo_stacked",
            "prompt": f"Professional brand logo for {company_name}, {industry} company. {wordmark_dir} with {icon_dir}. Stacked vertical layout with icon on top and wordmark below. {mood} aesthetic. Vector art style, clean lines, white background, ultra high quality, professional branding"
        },
        {
            "name": "wordmark_only",
            "prompt": f"Wordmark logotype for {company_name}, {industry} brand. {wordmark_dir}. Text-only logo design, no icon. {mood} feeling. Professional typography, vector art, clean design, white background, ultra high quality branding, corporate wordmark"
        },
        {
            "name": "icon_only",
            "prompt": f"Icon symbol for {company_name}, {industry} brand. {icon_dir}. Standalone app icon / brand mark, no text. {mood} style. Vector art, minimalist, geometric if appropriate, clean design, white background, ultra high quality, professional brand mark, can work at small sizes"
        },
        {
            "name": "logo_square_format",
            "prompt": f"Square format logo for {company_name}, {industry}. {icon_dir} with {company_name} text. Designed for square social media profile picture and app icon. {mood} aesthetic. Centered composition, vector art, white background, ultra high quality"
        },
        {
            "name": "logo_construction_guide",
            "prompt": f"Logo construction guide for {company_name} showing clear space, minimum size, grid structure. Technical diagram with measurements, spacing guidelines, and proportions. Professional brand identity guidelines page, clean layout, white background"
        }
    ]
    
    headers = {
        "Authorization": f"Bearer {POYO_API_KEY}",
        "Content-Type": "application/json"
    }
    
    for i, variation in enumerate(variations):
        var_name = variation["name"]
        prompt = variation["prompt"]
        
        payload = {
            "model": POYO_MODEL,
            "input": {
                "prompt": prompt,
                "size": POYO_DEFAULT_SIZE,
                "resolution": POYO_DEFAULT_RESOLUTION
            }
        }
        
        try:
            print(f"   Generating {var_name} ({i+1}/{len(variations)})...")
            response = requests.post(POYO_API_ENDPOINT, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
            
            if 'data' in result and 'task_id' in result['data']:
                task_id = result['data']['task_id']
                logo_variations[var_name] = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "status": "submitted"
                }
                print(f"   ✅ {var_name}: Task ID {task_id}")
            else:
                logo_variations[var_name] = {
                    "task_id": None,
                    "prompt": prompt,
                    "status": "pending"
                }
                print(f"   ⚠️ {var_name}: Queued")
                
        except requests.exceptions.HTTPError as e:
            if "429" in str(e):
                print(f"   ⚠️ {var_name}: Rate limit - will retry later")
                logo_variations[var_name] = {
                    "task_id": None,
                    "prompt": prompt,
                    "status": "rate_limited"
                }
            else:
                print(f"   ⚠️ {var_name}: HTTP error - {e}")
                logo_variations[var_name] = {
                    "task_id": None,
                    "prompt": prompt,
                    "status": "error",
                    "error": str(e)
                }
        except Exception as e:
            print(f"   ⚠️ {var_name}: Unexpected error - {e}")
            logo_variations[var_name] = {
                "task_id": None,
                "prompt": prompt,
                "status": "error",
                "error": str(e)
            }
    
    print(f"   ✅ Logo system generation complete: {len(logo_variations)} variations")
    return logo_variations


@tool
def generate_brand_applications(brand_info: Dict) -> Dict:
    """
    Generates mockups of brand applications using Poyo.ai.
    
    Creates:
    - Business Card design
    - Letterhead A4
    - Envelope designs (DL)
    - Notepad
    - ID Card / Badge
    - App Icon / Website Favicon
    - Social Media Templates
    
    Args:
        brand_info: Dictionary with brand visual identity
    
    Returns:
        Dictionary with task IDs for all application mockups
    """
    print("📱 [BRAND APPLICATIONS]  Generating brand application mockups...")
    
    company_name = brand_info.get('company_name', 'Brand')
    primary_color = brand_info.get('primary_colors_hex', ['#0066CC'])[0]
    industry = brand_info.get('industry', 'Technology')
    
    applications = {}
    
    mockups = [
        {
            "name": "business_card",
            "prompt": f"Professional business card design mockup for {company_name}, {industry} company. Front and back view. Modern minimalist layout, {primary_color} accent color, clean typography, {company_name} logo, contact information placeholders. High quality mockup, realistic presentation, white background"
        },
        {
            "name": "letterhead_a4",
            "prompt": f"A4 letterhead stationery design for {company_name}. {company_name} logo at top, professional layout, {primary_color} header/footer accents, clean typography grid, contact info in footer. Corporate stationery mockup, white paper, professional presentation"
        },
        {
            "name": "envelope_dl",
            "prompt": f"DL envelope design for {company_name}. {company_name} logo, return address area, {primary_color} accents. Professional corporate stationery, clean design, realistic mockup, white background"
        },
        {
            "name": "app_icon",
            "prompt": f"Mobile app icon for {company_name}, {industry} app. Square format, iOS/Android style. Simplified version of brand icon, {primary_color} color scheme, works at small size, modern app icon design, clean professional look"
        },
        {
            "name": "notepad",
            "prompt": f"Branded notepad design for {company_name}. A6 size, {company_name} logo at top, lined or grid pages, {primary_color} accent. Professional stationery mockup, realistic presentation"
        }
    ]
    
    headers = {
        "Authorization": f"Bearer {POYO_API_KEY}",
        "Content-Type": "application/json"
    }
    
    for i, mockup in enumerate(mockups):
        name = mockup["name"]
        prompt = mockup["prompt"]
        
        payload = {
            "model": POYO_MODEL,
            "input": {
                "prompt": prompt,
                "size": POYO_DEFAULT_SIZE,
                "resolution": POYO_DEFAULT_RESOLUTION
            }
        }
        
        try:
            print(f"   Generating {name} ({i+1}/{len(mockups)})...")
            response = requests.post(POYO_API_ENDPOINT, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
            
            if 'data' in result and 'task_id' in result['data']:
                applications[name] = {
                    "task_id": result['data']['task_id'],
                    "prompt": prompt,
                    "status": "submitted"
                }
                print(f"   ✅ {name}: Submitted")
            else:
                applications[name] = {"status": "pending", "prompt": prompt}
                print(f"   ⚠️ {name}: Queued")
                
        except requests.exceptions.HTTPError as e:
            if "429" in str(e):
                applications[name] = {"status": "rate_limited", "prompt": prompt}
                print(f"   ⚠️ {name}: Rate limit")
            else:
                applications[name] = {"status": "error", "error": str(e)}
                print(f"   ⚠️ {name}: Error - {e}")
        except Exception as e:
            applications[name] = {"status": "error", "error": str(e)}
            print(f"   ⚠️ {name}: Error - {e}")
    
    print(f"   ✅ Brand applications complete: {len(applications)} items")
    return applications


@tool  
def generate_scientific_color_palette(mood: str, industry: str = "skincare") -> Dict:
    """
    Generates professional color palette with primary and secondary colors.
    
    Returns:
        Dictionary with primary_colors, secondary_colors, color_meanings, usage_rules
    """
    print(f"🎨 [COLOR SYSTEM] Generating professional color palette...")
    print(f"   Mood: {mood}")
    print(f"   Industry: {industry}")
    
    # Scientific/Healthcare color palettes
    if "scientific" in mood.lower() or "medical" in mood.lower() or "skincare" in industry.lower():
        return {
            "primary_colors": {
                "brand_primary": "#2D5F8D",  # Trustworthy blue
                "brand_secondary": "#E8F1F5",  # Soft blue-grey
                "accent": "#6BA3C8"  # Calming blue
            },
            "secondary_colors": {
                "success_green": "#4CAF7A",  # Healthy skin green
                "warning_amber": "#F4A261",  # Attention/caution
                "info_teal": "#2A9D8F",  # Information
                "neutral_grey": "#F8F9FA"  # Background
            },
            "color_meanings": {
                "#2D5F8D": "Trust, professionalism, scientific accuracy",
                "#E8F1F5": "Cleanliness, clarity, breathability",
                "#6BA3C8": "Calm, supportive, approachable",
                "#4CAF7A": "Health, growth, positive results",
                "#F4A261": "Importance, gentle warning",
                "#2A9D8F": "Technology, innovation",
                "#F8F9FA": "Clean slate, neutrality"
            },
            "usage_rules": {
                "primary_use": "Buttons, headers, key UI elements",
                "secondary_use": "Backgrounds, cards, sections",
                "accent_use": "Highlights, links, interactive elements",
                "success_use": "Progress indicators, achievements",
                "warning_use": "Important notices, alerts",
                "neutral_use": "Backgrounds, containers"
            }
        }
    
    # Default professional palette
    return {
        "primary_colors": {
            "brand_primary": "#0066CC",
            "brand_secondary": "#F0F4F8",
            "accent": "#FF6B35"
        },
        "secondary_colors": {
            "success": "#10B981",
            "warning": "#F59E0B",
            "info": "#3B82F6",
            "neutral": "#F3F4F6"
        },
        "color_meanings": {
            "#0066CC": "Professional, trustworthy",
            "#F0F4F8": "Clean, modern",
            "#FF6B35": "Energy, action"
        },
        "usage_rules": {
            "primary_use": "Main brand touchpoints",
            "secondary_use": "Backgrounds, layouts",
            "accent_use": "CTAs, highlights"
        }
    }
