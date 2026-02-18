from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from state import BrandState
from tools.research_tools import market_competitor_analysis, audience_profiling
from schemas import MarketAnalysisSchema
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, LLM_TEMPERATURE_RESEARCH, REQUEST_TIMEOUT, LLM_PROVIDER
import json

# Initialize LLM - Supports both GitHub Models and OpenAI
llm = ChatOpenAI(
    model=LLM_MODEL,  # gpt-4o
    temperature=LLM_TEMPERATURE_RESEARCH,  # 0.0 for deterministic research
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
    timeout=REQUEST_TIMEOUT,  # 120 seconds
    max_retries=3
)
print(f"[RESEARCH AGENT] Using LLM provider: {LLM_PROVIDER}")

def research_agent(state: BrandState) -> BrandState:
    """
    Agent responsible for conducting market research and audience analysis.
    """
    print("[RESEARCH AGENT] Starting research phase...")
    
    brief = state["client_brief"]
    industry = brief.get("industry", "Technology")
    target_audience = brief.get("target_audience", "General Public")
    
    # 1. Competitor Analysis via Tool
    competitors = market_competitor_analysis.invoke({"industry": industry, "count": 3})
    
    # 2. Audience Profiling via Tool
    audience_insights = audience_profiling.invoke({"industry": industry, "target_demographic": target_audience})
    
    # 3. Synthesize findings using LLM with JSON mode (GitHub Models compatible)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert market researcher. Analyze the following data and provide a structured summary."),
        ("user", """Competitors: {competitors}
Audience: {audience}

Provide your analysis in valid JSON format with this exact structure:
{{
  "market_analysis": {{
    "insights": "detailed insights about market trends, size, and opportunities",
    "key_findings": "main findings from the research"
  }},
  "competitor_map": {{
    "positioning": "competitive positioning analysis",
    "key_players": "list of key competitors and their strengths"
  }}
}}

Output only valid JSON, no markdown, no code blocks, no other text.""")
    ])
    
    # Use LLM without response_format to avoid parse() call
    chain = prompt | llm
    
    response = chain.invoke({
        "competitors": json.dumps(competitors),
        "audience": json.dumps(audience_insights)
    })
    
    # Parse and validate the JSON response
    try:
        analysis_dict = json.loads(response.content)
        analysis_data = MarketAnalysisSchema(**analysis_dict)
    except (json.JSONDecodeError, Exception) as e:
        print(f"   ⚠️ JSON parsing failed, using fallback: {e}")
        # Fallback to simple dict
        analysis_data = MarketAnalysisSchema(
            market_analysis={"insights": str(response.content)[:500], "key_findings": "See raw response"},
            competitor_map={"positioning": "Analysis pending", "key_players": str(competitors)[:200]}
        )

    # Update state with validated structured output
    return {
        **state,
        "research_outputs": {
            "market_analysis": analysis_data.market_analysis,
            "audience_insights": audience_insights,
            "competitor_map": analysis_data.competitor_map
        },
        "approval_status": {**state["approval_status"], "research_approved": False}  # Requires human approval
    }
