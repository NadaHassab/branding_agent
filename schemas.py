"""
Pydantic schemas for structured LLM outputs.
These ensure type-safe, validated responses from the language models.
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Any


class MarketAnalysisSchema(BaseModel):
    """Schema for market research analysis output"""
    market_analysis: Dict[str, Any] = Field(description="Summary of market trends, size, and opportunities")
    competitor_map: Dict[str, Any] = Field(description="Positioning and analysis of key competitors")


class StrategySchema(BaseModel):
    """Schema for brand strategy output"""
    positioning: str = Field(description="A single compelling positioning statement")
    personality: List[str] = Field(description="List of 3-5 brand personality traits")
    messaging_framework: Dict[str, str] = Field(description="Key messages including tagline, value prop, and mission")
    name_options: List[str] = Field(description="3 creative brand name ideas")


class DesignDirectionSchema(BaseModel):
    """Schema for comprehensive design direction output"""
    # Logo Design
    wordmark_direction: str = Field(description="Detailed creative direction for wordmark/logotype design")
    icon_direction: str = Field(description="Detailed creative direction for standalone icon/symbol design")
    combined_logo_direction: str = Field(description="How wordmark and icon combine in full logo")
    
    # Visual Elements
    primary_colors_hex: List[str] = Field(description="3-5 primary brand colors as HEX codes")
    secondary_colors_hex: List[str] = Field(description="3-5 secondary/accent colors as HEX codes")
    
    # Typography
    primary_font_family: str = Field(description="Primary font for headlines/display")
    secondary_font_family: str = Field(description="Secondary font for body text")
    
    # Design System
    design_keywords: List[str] = Field(description="5+ design keywords (e.g., minimal, scientific, trustworthy)")
    mood_board: str = Field(description="Description of overall visual mood and aesthetic")
    grid_system: str = Field(description="Grid system description (e.g., 12-column, 8pt baseline)")
    
    # Rationale
    design_rationale: str = Field(description="Comprehensive explanation of all design choices")
