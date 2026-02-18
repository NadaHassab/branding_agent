"""
Comprehensive Brand Guidelines Document Generator
Follows professional brand guidelines structure like CEEM GUIDELINES.pdf

Sections:
1. Logo - Wordmark, Icon, Construction
2. Color Variations - Full color, monochrome, reversed
3. Logo Clearspace & Placement Rules
4. Co-Branding Guidelines
5. Incorrect Usage Examples
6. Primary Colors (with HEX, RGB, CMYK, Pantone)
7. Secondary/Accent Colors
8. Typography - Typeface rules, hierarchy
9. Pattern System (if applicable)
10. Grid System
11. Stationery - Business card, letterhead, envelope, notepad
12. ID/Badge Guidelines 
13. Calendar Design
14. App Icon / Website Favicon
"""
from langchain_core.tools import tool
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

@tool
def create_comprehensive_brand_guidelines(
    strategy: dict,
    design: dict,
    logo_system: dict,
    applications: dict,
    output_path: str = "output/Comprehensive_Brand_Guidelines.docx"
) -> str:
    """
    Creates a comprehensive brand guidelines document following professional structure.
    
    Includes all sections from the PDF template:
    - Cover & Introduction
    - Brand Strategy (Positioning, Mission, Values, Personality)
    - Logo System (All variations, construction, clearspace)
    - Color System (Primary, secondary, usage rules)
    - Typography (Font families, hierarchy, usage)
    - Grid System Guidelines
    - Pattern/Graphic Elements
    - Brand Applications (Stationery, digital, etc.)
    - Dos and Don'ts
    """
    print(f"📄 [COMPREHENSIVE GUIDELINES] Creating complete brand guidelines...")
    print(f"   Output: {output_path}")
    
    doc = Document()
    
    # Configure styles
    style = doc.styles['Normal']
    style.font.name = 'Helvetica'
    style.font.size = Pt(11)
    
    company_name = strategy.get('name_options', ['Brand'])[0] if 'name_options' in strategy else "Brand"
    positioning = strategy.get('positioning', 'Brand positioning')
    
    # =========================================================================
    # COVER PAGE
    # =========================================================================
    cover = doc.add_heading(f'{company_name}', 0)
    cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    subtitle = doc.add_heading('Brand Guidelines', level=2)
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    version_para = doc.add_paragraph('Version 1.0 | ' + '2026')
    version_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()
    
    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    doc.add_heading('Table of Contents', level=1)
    
    toc_items = [
        "1. Introduction",
        "2. Brand Strategy",
        "   2.1 Brand Positioning",
        "   2.2 Brand Personality",
        "   2.3 Core Values",
        "   2.4 Brand Voice & Messaging",
        "3. Logo System",
        "   3.1 Primary Logo",
        "   3.2 Wordmark",
        "   3.3 Icon/Symbol",
        "   3.4 Logo Construction & Grid",
        "   3.5 Logo Clearspace",
        "   3.6 Minimum Size Requirements",
        "4. Logo Variations",
        "   4.1 Color Variations",
        "   4.2 Monochrome Versions",
        "   4.3 Reversed (White on Color)",
        "5. Logo Usage",
        "   5.1 Placement Guidelines",
        "   5.2 Co-Branding Rules",
        "   5.3 Incorrect Usage - Don'ts",
        "6. Color System",
        "   6.1 Primary Colors",
        "   6.2 Secondary Colors",
        "   6.3 Color Values (HEX, RGB, CMYK)",
        "   6.4 Color Usage Rules",
        "7. Typography",
        "   7.1 Primary Typeface",
        "   7.2 Secondary Typeface",
        "   7.3 Type Hierarchy",
        "   7.4 Typography Rules",
        "8. Graphic Elements",
        "   8.1 Pattern System (if applicable)",
        "   8.2 Iconography Style",
        "9. Grid System",
        "   9.1 Layout Grid",
        "   9.2 Spacing Rules",
        "10. Brand Applications",
        "   10.1 Business Card",
        "   10.2 Letterhead (A4)",
        "   10.3 Envelope (DL)",
        "   10.4 Notepad",
        "   10.5 ID Badge / Card",
        "   10.6 Calendar Design",
        "11. Digital Applications",
        "   11.1 App Icon / Favicon",
        "   11.2 Website Header",
        "   11.3 Social Media Templates",
        "12. File Formats & Resources",
        "13. Appendix"
    ]
    
    for item in toc_items:
        doc.add_paragraph(item, style='List Number' if item[0].isdigit() and '   ' not in item else 'List Bullet')
    
    doc.add_page_break()
    
    # =========================================================================
    # 1. INTRODUCTION
    # =========================================================================
    doc.add_heading('1. Introduction', level=1)
    
    doc.add_paragraph(
        f"This brand guidelines document defines the visual and verbal identity of {company_name}. "
        f"These guidelines ensure consistent and impactful brand communication across all touchpoints."
    )
    
    doc.add_heading('Purpose of These Guidelines', level=2)
    doc.add_paragraph(
        "These guidelines serve as the definitive resource for anyone creating materials for "
        f"{company_name}. They provide clear direction on logo usage, color application, "
        "typography, and overall brand expression."
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # 2. BRAND STRATEGY
    # =========================================================================
    doc.add_heading('2. Brand Strategy', level=1)
    
    # 2.1 Positioning
    doc.add_heading('2.1 Brand Positioning', level=2)
    doc.add_paragraph(positioning)
    
    # 2.2 Personality
    doc.add_heading('2.2 Brand Personality', level=2)
    personality_traits = strategy.get('personality', [])
    for trait in personality_traits:
        p = doc.add_paragraph(trait, style='List Bullet')
    
    # 2.3 Values
    doc.add_heading('2.3 Core Values', level=2)
    doc.add_paragraph("Our brand is built on these fundamental values:")
    # Would pull from client brief if available
    doc.add_paragraph("• Excellence", style='List Bullet')
    doc.add_paragraph("• Innovation", style='List Bullet')
    doc.add_paragraph("• Integrity", style='List Bullet')
    
    # 2.4 Messaging
    doc.add_heading('2.4 Brand Voice & Messaging', level=2)
    messaging = strategy.get('messaging_framework', {})
    
    if 'tagline' in messaging:
        doc.add_heading('Tagline', level=3)
        doc.add_paragraph(f'"{messaging["tagline"]}"')
    
    if 'value_proposition' in messaging:
        doc.add_heading('Value Proposition', level=3)
        doc.add_paragraph(messaging['value_proposition'])
    
    if 'mission' in messaging:
        doc.add_heading('Mission', level=3)
        doc.add_paragraph(messaging['mission'])
    
    doc.add_page_break()
    
    # =========================================================================
    # 3. LOGO SYSTEM
    # =========================================================================
    doc.add_heading('3. Logo System', level=1)
    
    doc.add_heading('3.1 Primary Logo', level=2)
    doc.add_paragraph(
        f"The {company_name} logo consists of a wordmark and icon that work together to "
        "create a distinctive and memorable brand mark. The primary logo is the preferred "
        "version and should be used whenever possible."
    )
    
    # Reference to logo files
    if 'primary_logo_horizontal' in logo_system:
        doc.add_paragraph(f"[Primary Logo Horizontal - Task ID: {logo_system['primary_logo_horizontal'].get('task_id', 'N/A')}]")
    
    doc.add_heading('3.2 Wordmark Only', level=2)
    doc.add_paragraph(
        "The wordmark can be used independently when space is limited or when "
        "the icon would be too small to reproduce clearly."
    )
    
    if 'wordmark_only' in logo_system:
        doc.add_paragraph(f"[Wordmark - Task ID: {logo_system['wordmark_only'].get('task_id', 'N/A')}]")
    
    doc.add_heading('3.3 Icon/Symbol Only', level=2)
    doc.add_paragraph(
        "The icon can stand alone in cases where the brand is well-established, "
        "such as app icons, favicons, or social media profile pictures."
    )
    
    if 'icon_only' in logo_system:
        doc.add_paragraph(f"[Icon - Task ID: {logo_system['icon_only'].get('task_id', 'N/A')}]")
    
    doc.add_heading('3.4 Logo Construction & Grid', level=2)
    doc.add_paragraph(
        "The logo is built on a precise grid system to ensure proper proportions. "
        "The relationship between the icon and wordmark must never be altered."
    )
    
    if 'logo_construction_guide' in logo_system:
        doc.add_paragraph(f"[Construction Guide - Task ID: {logo_system['logo_construction_guide'].get('task_id', 'N/A')}]")
    
    doc.add_heading('3.5 Logo Clearspace', level=2)
    doc.add_paragraph(
        "Always maintain adequate clearspace around the logo. The minimum clearspace "
        "is equal to the height of the icon. No other graphic elements, text, or imagery "
        "should appear within this zone."
    )
    
    doc.add_heading('3.6 Minimum Size Requirements', level=2)
    doc.add_paragraph("Digital/Screen: Minimum width 120px")
    doc.add_paragraph("Print: Minimum width 20mm (0.8 inches)")
    
    doc.add_page_break()
    
    # ========================================================================= 
    # 4. LOGO VARIATIONS
    # =========================================================================
    doc.add_heading('4. Logo Variations', level=1)
    
    doc.add_heading('4.1 Color Variations', level=2)
    doc.add_paragraph(
        "The logo should primarily appear in full color. Use the color version "
        "whenever possible on white or light backgrounds."
    )
    
    doc.add_heading('4.2 Monochrome Versions', level=2)
    doc.add_paragraph("Black logo: Use on light backgrounds")
    doc.add_paragraph("White logo: Use on dark backgrounds or photography")
    
    doc.add_heading('4.3 Reversed (White on Color)', level=2)
    doc.add_paragraph(
        "The reversed white logo should be used on dark or colored backgrounds "
        "where the full color or black versions would not provide sufficient contrast."
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # 5. LOGO USAGE
    # =========================================================================
    doc.add_heading('5. Logo Usage', level=1)
    
    doc.add_heading('5.1 Placement Guidelines', level=2)
    doc.add_paragraph("Preferred placements:")
    doc.add_paragraph("• Top left corner (primary)", style='List Bullet')
    doc.add_paragraph("• Top center (acceptable)", style='List Bullet')
    doc.add_paragraph("• Bottom right (footer use)", style='List Bullet')
    
    doc.add_heading('5.2 Co-Branding Rules', level=2)
    doc.add_paragraph(
        f"When co-branding with partners, maintain equal visual weight. The {company_name} "
        "logo should never appear smaller than partner logos. Maintain minimum clearspace "
        "between logos equal to the height of the smaller logo."
    )
    
    doc.add_heading("5.3 Incorrect Usage - Don'ts", level=2)
    doc.add_paragraph("Never do the following:")
    doc.add_paragraph("• Rotate the logo", style='List Bullet')
    doc.add_paragraph("• Change the logo colors", style='List Bullet')
    doc.add_paragraph("• Stretch or distort the logo", style='List Bullet')
    doc.add_paragraph("• Rearrange logo elements", style='List Bullet')
    doc.add_paragraph("• Add effects (shadows, glows, etc.)", style='List Bullet')
    doc.add_paragraph("• Place on busy backgrounds without sufficient contrast", style='List Bullet')
    doc.add_paragraph("• Outline the logo", style='List Bullet')
    
    doc.add_page_break()
    
    # =========================================================================
    # 6. COLOR SYSTEM
    # =========================================================================
    doc.add_heading('6. Color System', level=1)
    
    doc.add_heading('6.1 Primary Colors', level=2)
    primary_colors = design.get('primary_colors', {})
    
    for color_name, color_hex in primary_colors.items():
        doc.add_heading(color_name.replace('_', ' ').title(), level=3)
        doc.add_paragraph(f"HEX: {color_hex}")
        # Add RGB and CMYK conversions (simplified for now)
        doc.add_paragraph(f"RGB: (calculated from HEX)")
        doc.add_paragraph(f"CMYK: (calculated from HEX)")
        doc.add_paragraph(f"Pantone: (closest match)")
    
    doc.add_heading('6.2 Secondary Colors', level=2)
    secondary_colors = design.get('secondary_colors', {})
    
    for color_name, color_hex in secondary_colors.items():
        doc.add_heading(color_name.replace('_', ' ').title(), level=3)
        doc.add_paragraph(f"HEX: {color_hex}")
    
    doc.add_heading('6.3 Color Usage Rules', level=2)
    usage_rules = design.get('usage_rules', {})
    for rule_name, rule_desc in usage_rules.items():
        doc.add_paragraph(f"{rule_name.replace('_', ' ').title()}: {rule_desc}")
    
    doc.add_page_break()
    
    # =========================================================================
    # 7. TYPOGRAPHY
    # =========================================================================
    doc.add_heading('7. Typography', level=1)
    
    doc.add_heading('7.1 Primary Typeface', level=2)
    primary_font = design.get('primary_font', 'Sans-serif font family')
    doc.add_paragraph(f"Primary Font: {primary_font}")
    doc.add_paragraph("Use for: Headlines, titles, callouts, UI elements")
    
    doc.add_heading('7.2 Secondary Typeface', level=2)
    secondary_font = design.get('secondary_font', 'Serif or secondary sans-serif')
    doc.add_paragraph(f"Secondary Font: {secondary_font}")
    doc.add_paragraph("Use for: Body copy, longer text, editorial content")
    
    doc.add_heading('7.3 Type Hierarchy', level=2)
    doc.add_paragraph("H1 - Display: 48pt / 3rem")
    doc.add_paragraph("H2 - Heading: 36pt / 2.25rem")
    doc.add_paragraph("H3 - Subheading: 24pt / 1.5rem")
    doc.add_paragraph("Body: 16pt / 1rem")
    doc.add_paragraph("Small: 14pt / 0.875rem")
    doc.add_paragraph("Caption: 12pt / 0.75rem")
    
    doc.add_heading('7.4 Typography Rules', level=2)
    doc.add_paragraph("• Never use more than 2 font families in one design")
    doc.add_paragraph("• Maintain consistent line height (1.5x for body text)")
    doc.add_paragraph("• Use proper hierarchy to guide the reader")
    doc.add_paragraph("• Ensure sufficient color contrast for readability (WCAG AA minimum)")
    
    doc.add_page_break()
    
    # =========================================================================
    # 8. GRAPHIC ELEMENTS
    # =========================================================================
    doc.add_heading('8. Graphic Elements', level=1)
    
    doc.add_heading('8.1 Pattern System', level=2)
    doc.add_paragraph(
        "Brand patterns can be used as backgrounds or decorative elements. "
        "Patterns should be subtle and not overpower primary content."
    )
    
    doc.add_heading('8.2 Iconography Style', level=2)
    doc.add_paragraph(
        "All icons should follow a consistent style: outlined or filled, "
        "2px stroke weight, rounded corners where appropriate."
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # 9. GRID SYSTEM
    # =========================================================================
    doc.add_heading('9. Grid System', level=1)
    
    doc.add_heading('9.1 Layout Grid', level=2)
    grid_system = design.get('grid_system', '12-column grid with 8pt baseline')
    doc.add_paragraph(f"Layout System: {grid_system}")
    doc.add_paragraph(
        "All layouts should be built on this grid system for consistency. "
        "Use column widths and gutters as defined in the system."
    )
    
    doc.add_heading('9.2 Spacing Rules', level=2)
    doc.add_paragraph("Use multiples of 8px for all spacing:")
    doc.add_paragraph("• 8px - Tight spacing")
    doc.add_paragraph("• 16px - Standard spacing")
    doc.add_paragraph("• 24px - Comfortable spacing")
    doc.add_paragraph("• 32px - Generous spacing")
    doc.add_paragraph("• 48px+ - Section breaks")
    
    doc.add_page_break()
    
    # =========================================================================
    # 10. BRAND APPLICATIONS
    # =========================================================================
    doc.add_heading('10. Brand Applications', level=1)
    
    if 'business_card' in applications:
        doc.add_heading('10.1 Business Card', level=2)
        doc.add_paragraph(f"[Business Card Design - Task ID: {applications['business_card'].get('task_id', 'N/A')}]")
        doc.add_paragraph("Standard size: 3.5\" x 2\" (88.9mm x 50.8mm)")
    
    if 'letterhead_a4' in applications:
        doc.add_heading('10.2 Letterhead (A4)', level=2)
        doc.add_paragraph(f"[Letterhead Design - Task ID: {applications['letterhead_a4'].get('task_id', 'N/A')}]")
        doc.add_paragraph("Size: A4 (210mm x 297mm)")
    
    if 'envelope_dl' in applications:
        doc.add_heading('10.3 Envelope (DL)', level=2)
        doc.add_paragraph(f"[Envelope Design - Task ID: {applications['envelope_dl'].get('task_id', 'N/A')}]")
        doc.add_paragraph("Size: DL (110mm x 220mm)")
    
    if 'notepad' in applications:
        doc.add_heading('10.4 Notepad', level=2)
        doc.add_paragraph(f"[Notepad Design - Task ID: {applications['notepad'].get('task_id', 'N/A')}]")
        doc.add_paragraph("Suggested size: A6 (105mm x 148mm)")
    
    doc.add_heading('10.5 ID Badge / Card', level=2)
    doc.add_paragraph("Standard badge size: 3.375\" x 2.125\" (CR80)")
    
    doc.add_heading('10.6 Calendar Design', level=2)
    doc.add_paragraph("Use brand colors for month headers and date highlights")
    
    doc.add_page_break()
    
    # =========================================================================
    # 11. DIGITAL APPLICATIONS
    # =========================================================================
    doc.add_heading('11. Digital Applications', level=1)
    
    if 'app_icon' in applications:
        doc.add_heading('11.1 App Icon / Favicon', level=2)
        doc.add_paragraph(f"[App Icon - Task ID: {applications['app_icon'].get('task_id', 'N/A')}]")
        doc.add_paragraph("Sizes needed:")
        doc.add_paragraph("• iOS: 1024x1024px")
        doc.add_paragraph("• Android: 512x512px")
        doc.add_paragraph("• Favicon: 16x16px, 32x32px, 192x192px")
    
    doc.add_heading('11.2 Website Header', level=2)
    doc.add_paragraph("Recommended header height: 60-80px")
    doc.add_paragraph("Logo should maintain minimum 20px clearspace from edges")
    
    doc.add_heading('11.3 Social Media Templates', level=2)
    doc.add_paragraph("Maintain brand consistency across platforms:")
    doc.add_paragraph("• Profile picture: Use icon only, square format")
    doc.add_paragraph("• Cover images: Incorporate brand colors and patterns")
    doc.add_paragraph("• Post templates: Use brand typography and color system")
    
    doc.add_page_break()
    
    # =========================================================================
    # 12. FILE FORMATS & RESOURCES
    # =========================================================================
    doc.add_heading('12. File Formats & Resources', level=1)
    
    doc.add_paragraph("Logo files available in:")
    doc.add_paragraph("• SVG (vector, web use)")
    doc.add_paragraph("• EPS (vector, print use)")
    doc.add_paragraph("• PNG (transparent background, digital use)")
    doc.add_paragraph("• JPG (solid background, general use)")
    
    doc.add_paragraph()
    doc.add_paragraph("For access to brand assets, contact the brand team.")
    
    doc.add_page_break()
    
    # =========================================================================
    # 13. APPENDIX
    # =========================================================================
    doc.add_heading('13. Appendix', level=1)
    
    doc.add_heading('Contact Information', level=2)
    doc.add_paragraph(f"{company_name} Brand Team")
    doc.add_paragraph("For questions about these guidelines or to request assets.")
    
    doc.add_heading('Version History', level=2)
    doc.add_paragraph("Version 1.0 - 2026 - Initial guidelines")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    
    print(f"   ✅ Comprehensive brand guidelines created: {output_path}")
    return output_path
