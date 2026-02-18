"""
Skincare AI Advisor App - Comprehensive Brand Brief
Based on research from lovi.care, skinsyncapp.ai, getskinbliss.com
"""

SKINCARE_APP_BRIEF = {
    "company_name": "DermAI",  # Suggested name - scientific + AI
    "industry": "AI-Powered Skincare Technology",
    "target_audience": "Health-conscious females aged 18-35, tech-savvy, interested in personalized skincare solutions",
    "brand_type": "new",
    "budget_tier": "premium",
    "core_values": [
        "Scientific Accuracy",
        "Personalization",
        "Trustworthiness", 
        "Innovation",
        "Accessibility"
    ],
    "mission_statement": "Empowering women to make informed, unbiased skincare decisions through AI-powered analysis and personalized recommendations that serve only their best interests - not brands, not sponsors, just you.",
    
    # Additional context
    "key_features": [
        "AI-Powered Photo Skin Analysis (Gemini AI)",
        "Text-based symptom analysis",
        "Personalized skincare routine generation (Morning/Evening)",
        "Smart product recommendations within budget",
        "Ingredient compatibility checking",
        "Product comparison tools",
        "AI Chat Expert for skincare guidance",
        "Progress tracking with visual records",
        "Pharmacy locator for offline purchase"
    ],
    
    "unique_value_proposition": "The ONLY truly unbiased AI skincare advisor - we're not paid by brands, we don't push products. Our AI works exclusively for YOU, analyzing your unique skin and recommending what's genuinely best for your needs and budget, not what pays us commissions.",
    
    "brand_differentiators": [
        "100% Brand Agnostic - No sponsorships, no affiliations, no bias",
        "Customer-First Algorithm - Recommendations based purely on your skin analysis and budget",
        "Transparent Science - Clear explanations of why products are recommended",
        "Budget Democracy - Best products at ANY price point, from drugstore to luxury",
        "No Hidden Agenda - We make money from subscriptions, not brand kickbacks"
    ],
    
    "brand_personality": [
        "Scientific",
        "Approachable",
        "Trustworthy",
        "Modern",
        "Empowering"
    ],
    
    "visual_direction": {
        "mood": "Clean, scientific, feminine but not overly girly, professional healthcare meets modern tech",
        "avoid": "Egyptian themes, heavy luxury aesthetics, overly decorative elements",
        "inspiration": "Medical apps, skincare science, minimal tech interfaces, clean beauty brands"
    },
    
    "competitive_landscape": [
        "SkinSync - AI skin analysis",
        "SkinBliss - personalized skincare",
        "Lovi Care - health tracking",
        "Curology - prescription skincare",
        "Prose - personalized beauty"
    ]
}

# Detailed feature descriptions for context
FEATURE_DETAILS = {
    "ai_analysis": {
        "photo_analysis": "Upload up to 3 photos, AI detects skin type, concerns (acne, pores, wrinkles), overall health",
        "text_analysis": "Describe symptoms in own words for textual diagnosis",
        "rate_limiting": "Limited analyses shown via progress bar to manage API costs"
    },
    
    "personalization": {
        "assessment_quiz": "Multi-step journey: Basic Info → Skin Type → Medical History → Lifestyle → Budget → Goals",
        "routine_generation": "AI creates Morning/Evening routines based on assessment + analysis",
        "manual_entry": "Users can add existing products or customize routines"
    },
    
    "product_ecosystem": {
        "discovery": "Catalog with detailed ingredient lists",
        "ingredient_analysis": "Check if product ingredients suit user's analyzed skin type",
        "comparison": "Side-by-side comparison (effectiveness, ingredients, price)",
        "e_commerce": "Full cart & checkout functionality"
    },
    
    "support": {
        "ai_chat": "Conversational Expert personas with FAQ suggestions + chat history",
        "progress_tracking": "Visual record of past analyses to show skin improvement",
        "pharmacy_locator": "Map/list to find nearest stores"
    }
}
