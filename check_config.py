"""
API Configuration Verification Script
This script checks if all required API keys are properly configured.
"""
import os
from dotenv import load_dotenv

load_dotenv()

def check_env_var(var_name, required=True):
    """Check if an environment variable is set and not a placeholder"""
    value = os.getenv(var_name)
    
    if not value:
        status = "❌ NOT SET"
        return False, status
    elif value.startswith("your_") or value == "":
        status = "⚠️  PLACEHOLDER - Need to replace with actual key"
        return False, status
    else:
        # Hide most of the key for security
        masked_value = value[:8] + "..." + value[-4:] if len(value) > 12 else "***"
        status = f"✅ SET ({masked_value})"
        return True, status

def main():
    print("=" * 60)
    print("🔍 Brand Agent - API Configuration Check")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check GitHub Token
    print("1. GitHub Token (for GPT-4o LLM)")
    is_set, status = check_env_var("GITHUB_TOKEN", required=True)
    print(f"   {status}")
    if not is_set:
        print("   → Get from: GitHub Settings > Developer settings > Personal access tokens")
        all_good = False
    print()
    
    # Check Poyo API Key
    print("2. Poyo.ai API Key (for image generation)")
    is_set, status = check_env_var("POYO_API_KEY", required=True)
    print(f"   {status}")
    if not is_set:
        print("   → Get from: https://poyo.ai/")
        all_good = False
    print()
    
    # Check Serper API Key
    print("3. Serper API Key (for CrewAI search) - MOST IMPORTANT")
    is_set, status = check_env_var("SERPER_API_KEY", required=True)
    print(f"   {status}")
    if not is_set:
        print("   → Get FREE key from: https://serper.dev/")
        print("   → Sign up and copy your API key")
        print("   → Add to .env file: SERPER_API_KEY=your_key_here")
        all_good = False
    print()
    
    # Optional keys
    print("4. OpenAI API Key (optional backup)")
    is_set, status = check_env_var("OPENAI_API_KEY", required=False)
    print(f"   {status}")
    print()
    
    print("=" * 60)
    if all_good:
        print("✅ All required API keys are configured!")
        print("You're ready to run: python main_orchestrator.py")
    else:
        print("⚠️  Some required API keys are missing or not configured")
        print()
        print("📖 Next Steps:")
        print("1. Visit https://serper.dev/ and sign up for FREE")
        print("2. Copy your API key from the Serper dashboard")
        print("3. Open the .env file in this directory")
        print("4. Replace 'your_serper_api_key_here' with your actual key")
        print("5. Save the file and run this script again")
        print()
        print("📚 Full guide: See SETUP_GUIDE.md")
    print("=" * 60)
    
    return all_good

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
