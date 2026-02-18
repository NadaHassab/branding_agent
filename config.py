import os
from dotenv import load_dotenv

load_dotenv()

# =============================================================================
# API KEYS CONFIGURATION
# =============================================================================

# GitHub Models (for LLM - GPT-4o)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Poyo.ai (for Image Generation - Nano Banana Pro)
POYO_API_KEY = os.getenv("POYO_API_KEY")

# Serper (for CrewAI Search)
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# OpenAI (Alternative LLM provider)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional - Legacy support
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# =============================================================================
# LLM CONFIGURATION - Automatic Provider Selection
# =============================================================================

# Provider Selection (set to "github" or "openai")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # Changed default to openai due to GitHub Models connectivity issues

# GitHub Models Configuration
GITHUB_ENDPOINT = "https://models.github.ai/inference"
GITHUB_MODEL = "gpt-4o"

# OpenAI Configuration  
OPENAI_ENDPOINT = "https://api.openai.com/v1"
OPENAI_MODEL = "gpt-4o"

# Active Configuration (based on selected provider)
if LLM_PROVIDER == "openai":
    LLM_BASE_URL = OPENAI_ENDPOINT
    LLM_MODEL = OPENAI_MODEL
    LLM_API_KEY = OPENAI_API_KEY
else:  # github
    LLM_BASE_URL = GITHUB_ENDPOINT
    LLM_MODEL = GITHUB_MODEL
    LLM_API_KEY = GITHUB_TOKEN

VISION_MODEL = LLM_MODEL

# LLM Settings
LLM_TEMPERATURE_RESEARCH = 0.0  # Deterministic for research
LLM_TEMPERATURE_STRATEGY = 0.7  # Creative for strategy
LLM_TEMPERATURE_DESIGN = 0.7  # Creative for design

# =============================================================================
# IMAGE GENERATION CONFIGURATION - Poyo.ai Nano Banana Pro
# =============================================================================

POYO_API_ENDPOINT = "https://api.poyo.ai/api/generate/submit"
POYO_MODEL = "nano-banana-2"  # Nano Banana Pro
POYO_DEFAULT_SIZE = "1:1"  # Square format for logos
POYO_DEFAULT_RESOLUTION = "1K"  # 1024x1024

# =============================================================================
# CREWAI SEARCH CONFIGURATION
# =============================================================================

# Serper configuration is handled automatically by crewai-tools
# Just ensure SERPER_API_KEY is set in environment

# =============================================================================
# PROJECT PATHS
# =============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# AGENT CONFIGURATION
# =============================================================================

MAX_RETRIES = 3
REQUEST_TIMEOUT = 120  # seconds (increased for GitHub Models API)
CONNECT_TIMEOUT = 60  # seconds for connection establishment
