from langchain_core.tools import tool
from crewai_tools import SerperDevTool
from bs4 import BeautifulSoup
import requests
from typing import List, Dict
import os

# Initialize CrewAI search tool
# You'll need to set SERPER_API_KEY in your .env file
# Get free API key from https://serper.dev/
search_tool = SerperDevTool()

@tool
def market_competitor_analysis(industry: str, count: int = 5) -> List[Dict]:
    """
    Performs a market analysis to find top competitors in a given industry using CrewAI search.
    """
    print(f"🔍 [RESEARCH TOOL] Searching for competitors in {industry}...")
    
    search_query = f"top {industry} competitors companies market leaders"
    print(f"   Search query: {search_query}")
    
    try:
        # Use CrewAI's SerperDevTool to search
        search_results = search_tool._run(search_query=search_query)
        
        # Parse the results
        results = []
        
        # SerperDevTool returns a dict with 'organic' key containing search results
        if isinstance(search_results, dict) and 'organic' in search_results:
            # Extract organic search results
            organic_results = search_results['organic'][:count]
            for item in organic_results:
                results.append({
                    "name": item.get('title', f"Competitor {len(results)+1}"),
                    "summary": item.get('snippet', 'No description available'),
                    "url": item.get('link', '#')
                })
        elif isinstance(search_results, str):
            # Fallback for string results
            results = [{
                "name": f"{industry} Market Analysis",
                "summary": search_results[:500],
                "url": "#"
            }]
        
        if not results:
            raise ValueError("No search results returned")
        
        print(f"   ✅ Found {len(results)} competitor insights")
        return results
        
    except Exception as e:
        print(f"   ⚠️ CrewAI search failed: {e}")
        raise ValueError(f"Failed to search for competitors in {industry}. Error: {str(e)}. Make sure SERPER_API_KEY is set in .env")

@tool
def audience_profiling(industry: str, target_demographic: str) -> Dict:
    """
    Generates an audience profile based on industry and target demographic using CrewAI search.
    """
    print(f"👥 [RESEARCH TOOL] Profiling audience: {target_demographic} for {industry}...")
    
    # Create focused search query
    search_query = f"{target_demographic} {industry} consumer behavior trends preferences"
    print(f"   Search query: {search_query}")
    
    try:
        # Use CrewAI's SerperDevTool to search
        search_results = search_tool._run(search_query=search_query)
        
        insights = []
        
        # Parse the results - SerperDevTool returns a dict with 'organic' results
        if isinstance(search_results, dict) and 'organic' in search_results:
            # Extract organic search results
            organic_results = search_results['organic'][:5]  # Get top 5 results
            for item in organic_results:
                insights.append({
                    "source": item.get('title', f"Market Research {len(insights)+1}"),
                    "insight": item.get('snippet', 'No information available')
                })
        elif isinstance(search_results, str):
            # Fallback for string results
            insights = [{
                "source": f"{industry} Audience Analysis",
                "insight": search_results[:500]
            }]
        
        if not insights:
            raise ValueError("No search results returned")
        
        print(f"   ✅ Found {len(insights)} audience insights")
        
        return {
            "demographics": target_demographic,
            "research_insights": insights,
            "sources": [i['source'] for i in insights]
        }
        
    except Exception as e:
        print(f"   ⚠️ CrewAI search failed: {e}")
        raise ValueError(f"Failed to profile audience for {target_demographic} in {industry}. Error: {str(e)}. Make sure SERPER_API_KEY is set in .env")
