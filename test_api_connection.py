"""
Quick diagnostic test for LLM API connectivity
Tests if the configured API endpoint is reachable and working
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, REQUEST_TIMEOUT, LLM_PROVIDER
import time

def test_api_connection():
    """Test if configured LLM API is reachable"""
    print("=" * 80)
    print("LLM API CONNECTIVITY TEST")
    print("=" * 80)
    print()
    
    print(f"[CONFIG]")
    print(f"  Provider: {LLM_PROVIDER}")
    print(f"  Endpoint: {LLM_BASE_URL}")
    print(f"  Model: {LLM_MODEL}")
    print(f"  Timeout: {REQUEST_TIMEOUT} seconds")
    print(f"  Token: {LLM_API_KEY[:20] if LLM_API_KEY else 'NOT SET'}...")
    print()
    
    if not LLM_API_KEY:
        print("=" * 80)
        print("[ERROR] API key not configured!")
        print("=" * 80)
        print()
        print("To use OpenAI:")
        print("  1. Get an API key from: https://platform.openai.com/api-keys")
        print("  2. Set it in your environment:")
        print("     set OPENAI_API_KEY=sk-your-key-here")
        print("  3. Run this test again")
        print()
        return False
    
    try:
        print("[TEST 1] Initializing LLM client...")
        llm = ChatOpenAI(
            model=LLM_MODEL,
            temperature=0.0,
            api_key=LLM_API_KEY,
            base_url=LLM_BASE_URL,
            timeout=REQUEST_TIMEOUT,
            max_retries=2
        )
        print("[OK] Client initialized")
        print()
        
        print("[TEST 2] Sending simple test message...")
        start_time = time.time()
        
        response = llm.invoke([
            HumanMessage(content="Reply with just 'OK' if you receive this message")
        ])
        
        elapsed = time.time() - start_time
        print(f"[OK] Response received in {elapsed:.2f} seconds")
        print(f"[RESPONSE] {response.content}")
        print()
        
        print("[TEST 3] Testing JSON structured output...")
        start_time = time.time()
        
        response = llm.invoke([
            HumanMessage(content='''Return a JSON object with exactly this structure:
            {"status": "success", "message": "API is working"}
            
            Output only valid JSON, no markdown, no code blocks.''')
        ])
        
        elapsed = time.time() - start_time
        print(f"[OK] Response received in {elapsed:.2f} seconds")
        print(f"[RESPONSE] {response.content}")
        print()
        
        print("=" * 80)
        print(f"[SUCCESS] All tests passed! {LLM_PROVIDER.upper()} API is working correctly.")
        print("=" * 80)
        return True
        
    except Exception as e:
        print()
        print("=" * 80)
        print("[FAILED] API connectivity test failed")
        print("=" * 80)
        print(f"[ERROR TYPE] {type(e).__name__}")
        print(f"[ERROR MESSAGE] {str(e)}")
        print()
        
        # Provide diagnostic info
        print("[DIAGNOSTICS]")
        if "ConnectTimeout" in str(type(e)):
            print("  Issue: Connection timeout")
            print("  Possible causes:")
            print("    - Network connectivity issues")
            print("    - Firewall blocking the connection")
            print(f"    - {LLM_PROVIDER.upper()} API endpoint is not accessible")
            print("    - VPN/proxy interference")
            print()
            print("  Solutions:")
            print("    - Check internet connection")
            print("    - Try disabling VPN/proxy temporarily")
            print(f"    - Check if {LLM_BASE_URL} is accessible")
        elif "Timeout" in str(e):
            print("  Issue: Request timeout")
            print("  Solution: API is slow - timeout has been increased to 120s")
        elif "401" in str(e) or "Unauthorized" in str(e):
            print("  Issue: Authentication failed")
            print(f"  Solution: Check {LLM_PROVIDER.upper()}_API_KEY is valid")
        elif "404" in str(e):
            print("  Issue: Endpoint not found")
            print("  Solution: Verify endpoint is correct")
        else:
            print("  Unknown error - see full traceback above")
        
        print()
        import traceback
        traceback.print_exc()
        
        return False

if __name__ == "__main__":
    success = test_api_connection()
    
    if success:
        print("\n[NEXT STEP] You can now run: python run_production.py")
    else:
        print("\n[ACTION REQUIRED] Fix API connectivity issues before running production")

