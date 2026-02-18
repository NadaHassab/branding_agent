"""
Simple API Test - Verify all services are working
Tests: GitHub GPT-4o, Poyo.ai Nano Banana, CrewAI Search
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_github_gpt4o():
    """Test GitHub Models GPT-4o API"""
    print("🧪 Test 1: GitHub Models GPT-4o")
    print("-" * 60)
    
    try:
        from langchain_openai import ChatOpenAI
        from config import GITHUB_TOKEN, GITHUB_ENDPOINT, LLM_MODEL
        
        llm = ChatOpenAI(
            model=LLM_MODEL,
            temperature=0.7,
            api_key=GITHUB_TOKEN,
            base_url=GITHUB_ENDPOINT,
            timeout=30,  # 30 second timeout
            max_retries=2
        )
        
        print(f"   Model: {LLM_MODEL}")
        print(f"   Endpoint: {GITHUB_ENDPOINT}")
        print(f"   Calling API...")
        
        response = llm.invoke("Write a one-sentence brand positioning for a sustainable coffee shop.")
        
        print(f"   ✅ SUCCESS!")
        print(f"   Response: {response.content[:100]}...")
        return True
        
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        return False

def test_crewai_search():
    """Test CrewAI + Serper Search"""
    print("\n🧪 Test 2: CrewAI + Serper Search")
    print("-" * 60)
    
    try:
        from crewai_tools import SerperDevTool
        import os
        
        # Set environment variable
        os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY', '')
        
        search_tool = SerperDevTool()
        
        print(f"   Search Query: 'coffee shop market trends 2024'")
        print(f"   Searching...")
        
        # SerperDevTool needs to be called with _run() directly
        results = search_tool._run(search_query="coffee shop market trends 2024")
        
        print(f"   ✅ SUCCESS!")
        print(f"   Results type: {type(results)}")
        print(f"   Results: {str(results)[:150]}...")
        return True
        
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_poyo_api():
    """Test Poyo.ai Nano Banana Pro"""
    print("\n🧪 Test 3: Poyo.ai Nano Banana Pro")
    print("-" * 60)
    
    try:
        import requests
        from config import POYO_API_KEY, POYO_API_ENDPOINT, POYO_MODEL
        
        payload = {
            "model": POYO_MODEL,
            "input": {
                "prompt": "Simple coffee cup logo, minimalist, vector art",
                "size": "1:1",
                "resolution": "1K"
            }
        }
        
        headers = {
            "Authorization": f"Bearer {POYO_API_KEY}",
            "Content-Type": "application/json"
        }
        
        print(f"   Model: {POYO_MODEL}")
        print(f"   Endpoint: {POYO_API_ENDPOINT}")
        print(f"   Submitting image generation request...")
        
        response = requests.post(POYO_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        print(f"   ✅ SUCCESS!")
        print(f"   Response: {result}")
        return True
        
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("🔬 BRAND AGENT - API VERIFICATION TEST")
    print("=" * 60)
    print()
    
    results = {}
    
    # Test 1: GitHub GPT-4o
    results['gpt4o'] = test_github_gpt4o()
    
    # Test 2: CrewAI Search
    results['search'] = test_crewai_search()
    
    # Test 3: Poyo.ai
    results['poyo'] = test_poyo_api()
    
    # Summary
    print()
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"GitHub GPT-4o:        {'✅ PASS' if results['gpt4o'] else '❌ FAIL'}")
    print(f"CrewAI + Serper:      {'✅ PASS' if results['search'] else '❌ FAIL'}")
    print(f"Poyo.ai Nano Banana:  {'✅ PASS' if results['poyo'] else '❌ FAIL'}")
    print("=" * 60)
    
    if all(results.values()):
        print("✅ ALL TESTS PASSED - System ready for production!")
        return True
    else:
        print("⚠️  Some tests failed - check configuration above")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
