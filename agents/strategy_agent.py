from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from state import BrandState
from schemas import StrategySchema
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, LLM_TEMPERATURE_STRATEGY, REQUEST_TIMEOUT, LLM_PROVIDER
import json

# Initialize LLM - Supports both GitHub Models and OpenAI
llm = ChatOpenAI(
    model=LLM_MODEL,  # gpt-4o
    temperature=LLM_TEMPERATURE_STRATEGY,  # 0.7 for creative strategy
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
    timeout=REQUEST_TIMEOUT,  # 120 seconds
    max_retries=3
)
print(f"[STRATEGY AGENT] Using LLM provider: {LLM_PROVIDER}")

def strategy_agent(state: BrandState) -> BrandState:
    """
    Agent responsible for developing the brand strategy based on research.
    """
    print("[STRATEGY AGENT] Developing brand strategy...")
    
    brief = state["client_brief"]
    research = state["research_outputs"]
    
    # Prompt for strategy generation
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world-class Brand Strategist. Create a winning brand strategy."),
        ("user", """
        Client Brief: {brief}
        
        Research Insights: {research}
        
        Generate your response in valid JSON format with this exact structure:
        {{
          "positioning": "single compelling positioning statement",
          "personality": ["trait1", "trait2", "trait3"],
          "messaging_framework": {{
            "tagline": "brand tagline",
            "value_proposition": "key value proposition",
            "mission": "brand mission"
          }},
          "name_options": ["name1", "name2", "name3"]
        }}
        
        Output only valid JSON, no markdown, no code blocks, no other text.
        """)
    ])
    
    # Use LLM without response_format to avoid parse() call
    chain = prompt | llm
    
    response = chain.invoke({
        "brief": json.dumps(brief),
        "research": json.dumps(research)
    })
    
    # Parse and validate the JSON response
    try:
        strategy_dict = json.loads(response.content)
        strategy_data = StrategySchema(**strategy_dict)
    except (json.JSONDecodeError, Exception) as e:
        print(f"   ⚠️ JSON parsing failed, using fallback: {e}")
        # Fallback to simple dict
        strategy_data = StrategySchema(
            positioning="Strategic positioning pending",
            personality=["innovative", "customer-focused", "authentic"],
            messaging_framework={"tagline": "TBD", "value_proposition": "TBD", "mission": "TBD"},
            name_options=["Option 1", "Option 2", "Option 3"]
        )

    return {
        **state,
        "strategy_outputs": {
            "positioning": strategy_data.positioning,
            "personality": strategy_data.personality,
            "messaging_framework": strategy_data.messaging_framework,
            "name_options": strategy_data.name_options
        },
        "approval_status": {**state["approval_status"], "strategy_approved": False}  # Requires human approval
    }
