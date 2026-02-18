from typing import TypedDict, List, Dict, Any, Optional
from langchain_core.messages import BaseMessage

class ClientBrief(TypedDict):
    company_name: str
    industry: str
    target_audience: str
    brand_type: str  # "new" | "rebrand"
    budget_tier: str # "basic" | "premium" | "enterprise"
    core_values: List[str]
    mission_statement: str

class ResearchOutputs(TypedDict):
    market_analysis: Dict[str, Any]
    audience_insights: Dict[str, Any]
    competitor_map: Dict[str, Any]

class StrategyOutputs(TypedDict):
    positioning: str
    personality: List[str]
    messaging_framework: Dict[str, Any]
    name_options: List[str]

class DesignOutputs(TypedDict):
    logo_system: Dict[str, Any]  # 6 variations: horizontal, stacked, wordmark, icon, square, construction
    color_palette: Dict[str, Any]  # primary + secondary colors with meanings and usage rules
    typography: Dict[str, Any]  # hierarchy, font families, rules
    applications: Dict[str, Any]  # business card, letterhead, envelope, app icon, notepad
    grid_system: str  # grid specification
    design_direction: Dict[str, Any]  # full DesignDirectionSchema dict
    design_rationale: str

class Deliverables(TypedDict):
    strategy_doc: str
    brand_guidelines: str
    logo_system: Dict[str, Any]
    applications: Dict[str, Any]
    color_palette: Dict[str, Any]
    typography: Dict[str, Any]
    asset_summary: Dict[str, Any]

class ApprovalStatus(TypedDict):
    research_approved: bool
    strategy_approved: bool
    design_approved: bool

class BrandState(TypedDict):
    messages: List[BaseMessage]
    client_brief: ClientBrief
    research_outputs: Optional[ResearchOutputs]
    strategy_outputs: Optional[StrategyOutputs]
    design_outputs: Optional[DesignOutputs]
    deliverables: Optional[Deliverables]
    approval_status: ApprovalStatus
    next_step: str
    errors: List[str]
