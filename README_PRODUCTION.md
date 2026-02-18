# DermAI Brand Guidelines - Production System

## Overview
Professional brand identity system for DermAI - an unbiased AI-powered skincare advisor app targeting females 18-35.

## Key Differentiator
**100% UNBIASED** - No brand sponsorships, no affiliations, pure customer-first recommendations based on AI skin analysis and budget.

## System Architecture

### LangGraph + CrewAI Hybrid
- **LangGraph**: Provides state management, interrupt points for human review, conditional workflow edges
- **CrewAI**: Provides SerperDevTool for web search (not using full agent framework)

### Why This Architecture?
LangGraph offers features CrewAI alone doesn't provide for this workflow:
1. **State Persistence**: Maintains brand state across all agents
2. **Human-in-the-Loop**: Interrupt points before strategy/design for approval
3. **Conditional Edges**: Only proceed to design if strategy approved
4. **Checkpointing**: Resume from any point if interrupted

## Generated Deliverables

### 1. Brand Strategy Document
`output/Brand_Strategy.docx`
- Market Analysis
- Competitor Insights  
- Brand Positioning
- Messaging Framework
- Brand Personality

### 2. Comprehensive Brand Guidelines 
`output/Comprehensive_Brand_Guidelines.docx`

Following **CEEM GUIDELINES (2).pdf** professional structure:

#### Structure (42-page template):
1. **Cover Page** - Brand name, "Brand Guidelines", date
2. **Welcome** - Introduction to unified brand
3. **Table of Contents**
4. **Section 01: Overview**
   - About the brand
   - Mission, Vision, Purpose
5. **Section 02: The Logo**
   - Logo Lockup (Wordmark + Icon)
   - Logo Construction (Grid system, 14x proportions)  
   - Logo Variations (Linear horizontal, Stacked vertical)
   - Color Variations (full color, monochrome, reversed)
   - Logo Clearspace (Print: 25mm/10mm, Digital: 160px/75px)
   - Placement Rules (Left aligned primary, Right secondary, Center tertiary)
   - Co-Branding (1x spacing, partner logo max height = symbol height)
   - Incorrect Usage Examples
6. **Section 03: Colors**
   - Primary Colors (RGB, HEX, CMYK, Pantone)
   - Secondary Colors (Palettes for different moods)
7. **Section 04: Typography**
   - Primary Font (Headings/UI)
   - Secondary Font (Body copy)
   - Typeface Rules & Hierarchy (H1-H6, Body, Caption)
8. **Section 05: Pattern** (Brand graphic elements)
9. **Grid System** (12-column, 8pt baseline)
10. **Applications**
    - Business Card (3.5" x 2")
    - Letterhead (A4)
    - Envelope (DL)
    - App Icon (iOS/Android)
    - Notepad (A6)

## Visual Assets Generated

### Logo System (6 Variations)
Generated via Poyo.ai Nano Banana Pro:
1. **primary_logo_horizontal** - Icon left + wordmark right
2. **primary_logo_stacked** - Icon top + wordmark bottom  
3. **wordmark_only** - Text-based logo
4. **icon_only** - Standalone symbol for app icons
5. **logo_square_format** - Square composition for social media
6. **logo_construction_guide** - Grid, proportions, measurements

### Color Palette
- **Primary Colors**: 3 core brand colors (HEX, RGB, CMYK)
- **Secondary Colors**: 4 accent colors for variety
- **Color Meanings**: Assigned to each color
- **Usage Rules**: When to use primary vs secondary

### Typography System
- **Primary Font**: Poppins/Inter/Montserrat (for headings, UI)
- **Secondary Font**: Source Sans Pro/Open Sans/Lato (for body)
- **Hierarchy**: H1 (48pt), H2 (36pt), H3 (24pt), Body (16pt), Small (14pt), Caption (12pt)
- **Rules**: WCAG AA contrast, 1.5x line height, max 2 fonts

### Brand Applications
Generated mockups via Poyo.ai:
1. **Business Card** - Front/back, contact placeholders
2. **Letterhead (A4)** - Logo header, contact footer
3. **Envelope (DL)** - Logo, return address
4. **App Icon** - iOS/Android simplified brand mark
5. **Notepad (A6)** - Branded stationery

## API Configuration

### GitHub Models GPT-4o
```python
LLM_MODEL = "gpt-4o"
GITHUB_TOKEN = "github_pat_..."
GITHUB_ENDPOINT = "https://models.github.ai/inference"
```

**Temperatures**:
- Research: 0.0 (factual)
- Strategy/Design: 0.7 (creative)

### Poyo.ai Nano Banana Pro
```python
POYO_MODEL = "nano-banana-2"
POYO_API_KEY = "psk-..."
POYO_DEFAULT_SIZE = "1:1"
POYO_DEFAULT_RESOLUTION = "1K"
```

Rate limits: Increased per user request

### Serper API (CrewAI Search)
```python
SERPER_API_KEY = "9286dd24f4e436dd602d4547098f81d0ff838aae"
```
Free tier: 2500 searches/month

## File Structure

```
brand_agent/
├── config.py                          # API keys, endpoints
├── state.py                           # Pydantic state definitions
├── schemas.py                         # Structured output schemas
├── main_orchestrator.py               # LangGraph workflow
├── skincare_brief.py                  # DermAI brand brief
├── agents/
│   ├── research_agent.py              # Market/competitor research
│   ├── strategy_agent.py              # Brand positioning
│   ├── design_agent.py                # Visual identity (UPDATED)
│   └── deliverables_agent.py          # Document generation (UPDATED)
├── tools/
│   ├── research_tools.py              # Serper search
│   ├── design_tools.py                # Basic logo gen (LEGACY)
│   ├── comprehensive_design_tools.py  # NEW: Complete brand system
│   ├── comprehensive_guidelines.py    # NEW: Professional DOCX gen
│   └── document_tools.py              # Strategy doc gen
├── output/
│   ├── Brand_Strategy.docx            # GENERATED
│   └── Comprehensive_Brand_Guidelines.docx  # GENERATED
├── CEEM GUIDELINES (2).pdf            # Template reference
├── test_skincare_comprehensive.py     # Full system test
├── run_production.py                  # NEW: Production runner
└── README_PRODUCTION.md               # This file
```

## Running the System

### Production Mode
```powershell
python run_production.py
```

### Test Mode
```powershell
python test_skincare_comprehensive.py
```

### What Happens:
1. **Research Agent**: Searches competitors in "AI-Powered Skincare Technology"
2. **Strategy Agent**: Generates positioning emphasizing unbiased, customer-first approach
3. **Design Agent**: Creates comprehensive visual identity (6 logos, colors, typography, grid, 5 applications)
4. **Deliverables Agent**: Generates professional DOCX documents following CEEM structure

## Output Files

After running, check `output/` folder:

### 1. Brand_Strategy.docx (~37KB)
- Market analysis findings
- Audience insights
- Competitor mapping
- Brand positioning statement
- Messaging framework (tagline, value prop, mission)
- Brand personality traits
- Name options

### 2. Comprehensive_Brand_Guidelines.docx (~40KB)
Complete professional brand guidelines with:
- Welcome & TOC
- Brand overview (about, mission, vision, purpose)
- Logo system (all variations, construction, rules)
- Color system (primary/secondary with codes)
- Typography (fonts, hierarchy, usage rules)
- Grid system & spacing
- Brand applications
- Usage dos and don'ts

## Poyo.ai Task Management

### Checking Task Status
If logo/application generation tasks were created:

```powershell
# Check task status
curl -H "Authorization: Bearer $env:POYO_API_KEY" https://api.poyo.ai/task/{task_id}

# Download generated image (when ready)
curl -H "Authorization: Bearer $env:POYO_API_KEY" https://api.poyo.ai/task/{task_id}/download -o logo.png
```

### Rate Limiting
- System gracefully handles rate limits
- Returns task IDs even if rate limited
- Can retrieve images later when rate limit resets
- User increased rate limit for production use

## Brand Brief Summary

### DermAI - AI Skincare Advisor

**Target**: Health-conscious females 18-35, tech-savvy

**Core Values**:
- Scientific Accuracy
- Personalization  
- Trustworthiness
- Innovation
- Accessibility

**Mission**: Empowering women to make informed, unbiased skincare decisions through AI-powered analysis

**Unique Value Proposition**: The ONLY truly unbiased AI skincare advisor - not paid by brands, recommendations based purely on skin analysis and budget

**Brand Differentiators**:
1. 100% Brand Agnostic - No sponsorships, no affiliations
2. Customer-First Algorithm - Recommendations based on YOUR skin only
3. Transparent Science - Clear explanations
4. Budget Democracy - Best products at ANY price point
5. No Hidden Agenda - Revenue from subscriptions, not brand kickbacks

**Key Features**:
- AI-Powered Photo Skin Analysis (Gemini AI)
- Text-based symptom analysis
- Personalized routines (Morning/Evening)
- Smart product recommendations within budget
- Ingredient compatibility checking
- Product comparison tools
- AI Chat Expert for guidance
- Progress tracking with visual records
- Pharmacy locator

**Competitors**: 
- lovi.care
- skinsyncapp.ai  
- getskinbliss.com
- SkinSync
- SkinBliss
- Curology
- Prose

## Design Direction

### Wordmark
Modern sans-serif with clean, geometric letterforms. Slightly rounded corners for balance between professionalism and approachability. Lowercase or mixed case for warmth.

### Icon
Abstract interpretation of skin cell structure or molecular pattern. Interconnected geometric elements symbolizing scientific precision + personalization. Simplified enough to work at small sizes (app icons).

### Mood
Clean minimalism meets scientific precision. Soft gradients, crisp white spaces, subtle geometric patterns. Professional healthcare aesthetic with modern tech sensibility. Feminine but not overly girly.

### Colors
Primary: Scientific blues/teals (trust, precision)
Secondary: Soft pinks/corals (feminine, skin-tone friendly), greens (health, natural)
Accent: Warm amber/coral (attention, warmth)

### Typography
- Primary: Poppins/Inter/Montserrat (modern, geometric, clean)
- Secondary: Source Sans Pro/Open Sans/Lato (readable, professional)

### Visual Avoidance
- Egyptian themes
- Heavy luxury aesthetics
- Overly decorative elements
- Dated beauty tropes

## Customization

### Updating Brand Brief
Edit `skincare_brief.py`:
```python
SKINCARE_APP_BRIEF = {
    "company_name": "Your Brand",
    "industry": "Your Industry",
    # ... customize all fields
}
```

### Adjusting Design Direction
Edit `schemas.py` to modify `DesignDirectionSchema` for different creative prompts.

### Changing PDF Structure
Edit `tools/comprehensive_guidelines.py` to match different brand guidelines template.

## Troubleshooting

### Unicode Encoding Errors (Windows)
```powershell
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

### Rate Limit Issues
- Poyo.ai: Wait for rate limit reset, task IDs preserved
- Serper: 2500/month free, upgrade if needed
- GitHub Models: Check quota

### Missing Dependencies
```powershell
pip install -r requirements.txt
```

### API Key Issues
Check `config.py` and `.env` for correct keys:
- `GITHUB_TOKEN`
- `POYO_API_KEY`
- `SERPER_API_KEY`

## Next Steps

1. ✅ Review `output/Brand_Strategy.docx`
2. ✅ Review `output/Comprehensive_Brand_Guidelines.docx`
3. ⏳ If Poyo.ai tasks generated, check status and download images
4. ✏️ Insert generated logo/application images into guidelines DOCX
5. 📤 Export DOCX to PDF for distribution
6. 🎨 Use design specifications to create additional assets
7. 📱 Implement brand identity across app UI/UX

## Support

For questions or issues:
- Check terminal output for detailed logs
- Review error messages in context
- Verify API keys and quotas
- Test with `test_skincare_comprehensive.py` first

---

**Generated**: February 14, 2026  
**System Version**: 1.0 - Production  
**Template**: CEEM GUIDELINES (2).pdf
