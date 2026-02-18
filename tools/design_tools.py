from langchain_core.tools import tool
from typing import List
import requests
import time
import os
from config import POYO_API_KEY, POYO_API_ENDPOINT, POYO_MODEL, POYO_DEFAULT_SIZE, POYO_DEFAULT_RESOLUTION

@tool
def generate_logo_concepts(keywords: List[str], style: str) -> List[str]:
    """
    Generates logo concepts using Poyo.ai Nano Banana Pro API.
    
    Model: Nano Banana 2 (nano-banana-2)
    API: Poyo.ai (https://poyo.ai)
    
    Args:
        keywords: List of design keywords (e.g., ['sustainable', 'modern', 'clean'])
        style: Overall design style (e.g., 'modern vector', 'minimalist')
    
    Returns:
        List of generated logo concept data (URLs or task IDs)
    """
    print(f"🎨 [DESIGN TOOL - POYO.AI] Generating logo concepts...")
    print(f"   Model: {POYO_MODEL}")
    print(f"   Keywords: {keywords}")
    print(f"   Style: {style}")
    
    logo_concepts = []
    
    # Generate 3 different logo concepts using Nano Banana Pro
    for i, keyword in enumerate(keywords[:3]):
        prompt = f"Professional {style} logo design for {keyword}, minimalist, corporate branding, vector art, clean design, white background, high quality"
        
        payload = {
            "model": POYO_MODEL,  # nano-banana-2
            "input": {
                "prompt": prompt,
                "size": POYO_DEFAULT_SIZE,  # 1:1 square
                "resolution": POYO_DEFAULT_RESOLUTION  # 1K (1024x1024)
            }
        }
        
        headers = {
            "Authorization": f"Bearer {POYO_API_KEY}",
            "Content-Type": "application/json"
        }
        
        try:
            print(f"   Generating concept {i+1}/3: {keyword}...")
            response = requests.post(POYO_API_ENDPOINT, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # Handle different response formats from Poyo.ai
            if 'data' in result and 'task_id' in result['data']:
                task_id = result['data']['task_id']
                logo_concepts.append(f"Logo Concept {i+1}: {keyword} - Task ID: {task_id}")
                print(f"   ✅ Submitted (Task ID: {task_id})")
            elif 'task_id' in result:
                logo_concepts.append(f"Logo Concept {i+1}: {keyword} - Task ID: {result['task_id']}")
                print(f"   ✅ Submitted (Task ID: {result['task_id']})")
            elif 'image_url' in result:
                logo_concepts.append(result['image_url'])
                print(f"   ✅ Generated: {result['image_url']}")
            else:
                logo_concepts.append(f"Logo Concept {i+1}: {keyword} (Prompt: {prompt})")
                print(f"   ✅ Queued for generation")
                
        except requests.exceptions.HTTPError as e:
            # Handle rate limiting and other HTTP errors gracefully
            if "429" in str(e) or "Too Many Requests" in str(e):
                print(f"   ⚠️ Rate limit hit for {keyword} - using fallback")
                logo_concepts.append(f"Logo Concept {i+1}: {keyword} style logo - [Rate limit exceeded, would be generated in production]")
            else:
                print(f"   ⚠️ HTTP error for {keyword}: {e} - using fallback")
                logo_concepts.append(f"Logo Concept {i+1}: {keyword} - [Error: {str(e)[:50]}]")
        except Exception as e:
            print(f"   ⚠️ Unexpected error for {keyword}: {e} - using fallback")
            logo_concepts.append(f"Logo Concept {i+1}: {keyword} - [Placeholder concept]")
    
    print(f"   ✅ All {len(logo_concepts)} logo concepts processed")
    return logo_concepts

@tool
def generate_color_palette(mood: str) -> List[str]:
    """
    Generates a color palette based on the intended brand mood.
    """
    print(f"🎨 [DESIGN TOOL] Generating color palette for mood: {mood}")
    
    # Simple lookup for demonstration. 
    # Real implementation could use Colormind API or LLM color theory generation.
    palettes = {
        "professional": ["#003366", "#FFFFFF", "#808080", "#000000"],
        "energetic": ["#FF5733", "#FFC300", "#FFFFFF", "#900C3F"],
        "eco-friendly": ["#2D5016", "#D4763E", "#F5F1E8", "#5D4037"],
        "luxury": ["#D4AF37", "#000000", "#FFFFFF", "#333333"]
    }
    
    # Return matched palette or a default one
    selected_palette = next((v for k, v in palettes.items() if k in mood.lower()), ["#333333", "#CCCCCC", "#FFFFFF", "#007BFF"])
    return selected_palette
