# 🏗️ Brand Agent System - Technical Stack

## Overview
AI-powered brand strategy and identity system using state-of-the-art models and tools.

---

## 🤖 Core Technologies

### 1. LLM - GitHub Models (GPT-4o)
**Purpose**: All natural language processing and reasoning

**Model**: `gpt-4o`  
**Endpoint**: `https://models.github.ai/inference`  
**Provider**: GitHub Models  
**API Key**: `GITHUB_TOKEN`

**Usage**:
- **Research Agent** (Temperature: 0.0) - Deterministic market analysis
- **Strategy Agent** (Temperature: 0.7) - Creative brand strategy  
- **Design Agent** (Temperature: 0.7) - Creative visual direction

**Why GPT-4o**:
- State-of-the-art reasoning
- Fast inference
- Excellent structured output support
- Free tier via GitHub Models

---

### 2. Image Generation - Poyo.ai (Nano Banana Pro)
**Purpose**: Logo and visual asset generation

**Model**: `nano-banana-2` (Nano Banana Pro)  
**Endpoint**: `https://api.poyo.ai/api/generate/submit`  
**Provider**: Poyo.ai  
**API Key**: `POYO_API_KEY`

**Specifications**:
- Default Size: `1:1` (Square)
- Default Resolution: `1K` (1024x1024)
- Format: High-quality PNG
- Style: Professional, vector art, minimal

**Why Nano Banana Pro**:
- Optimized for professional graphics
- Fast generation
- High-quality vector-style outputs
- Cost-effective

---

### 3. Web Search - CrewAI + Serper
**Purpose**: Real-time market research and competitor analysis

**Tool**: `SerperDevTool` from CrewAI  
**Search Engine**: Serper.dev  
**API Key**: `SERPER_API_KEY`

**Features**:
- Enterprise-grade search results
- 2,500 free searches/month
- Structured data output
- No rate limiting (unlike DuckDuckGo)

**Why CrewAI + Serper**:
- More reliable than free search APIs
- Structured, consistent results
- Built for AI agents
- Generous free tier

---

## 🧠 Framework & Architecture

### LangGraph
**Purpose**: Agent orchestration and workflow management

**Features**:
- State management across agents
- Conditional edges for human-in-the-loop
- Interrupt points for approval workflows
- Memory/checkpointing support

### LangChain
**Purpose**: LLM interaction and tool integration

**Features**:
- Structured output with Pydantic
- Tool/function calling
- Prompt templates
- Chain composition

---

## 📊 Data Flow

```
User Input (Brief)
    ↓
[Research Agent] → CrewAI/Serper Search
    ↓
[LLM Analysis] → GitHub GPT-4o (Structured Output)
    ↓
[Strategy Agent] → GitHub GPT-4o (Creative)
    ↓
⏸️ HUMAN APPROVAL CHECKPOINT
    ↓
[Design Agent] → GitHub GPT-4o (Direction)
    ↓
[Image Generation] → Poyo.ai Nano Banana Pro
    ↓
[Deliverables Agent] → PDF/DOCX Generation
    ↓
Final Brand Package
```

---

## 🔧 Configuration

All configuration is centralized in `config.py`:

### API Keys
```python
GITHUB_TOKEN       # GitHub Models (GPT-4o)
POYO_API_KEY       # Poyo.ai (Nano Banana Pro)
SERPER_API_KEY     # Serper (Search)
```

### LLM Settings
```python
LLM_MODEL = "gpt-4o"
GITHUB_ENDPOINT = "https://models.github.ai/inference"
LLM_TEMPERATURE_RESEARCH = 0.0   # Deterministic
LLM_TEMPERATURE_STRATEGY = 0.7   # Creative
LLM_TEMPERATURE_DESIGN = 0.7     # Creative
```

### Image Generation Settings
```python
POYO_MODEL = "nano-banana-2"
POYO_DEFAULT_SIZE = "1:1"
POYO_DEFAULT_RESOLUTION = "1K"
```

---

## 📦 Key Dependencies

```
langgraph          # Agent orchestration
langchain          # LLM framework
langchain-openai   # OpenAI-compatible API (GitHub Models)
crewai             # AI agent framework
crewai-tools       # Search tools (Serper)
pydantic           # Structured outputs
python-docx        # Word document generation
reportlab          # PDF generation
flask              # Web interface
```

---

## 🎯 Structured Outputs

All LLM responses use Pydantic schemas for type safety:

### MarketAnalysisSchema
```python
market_analysis: Dict  # Market trends, size, opportunities
competitor_map: Dict   # Competitor positioning
```

### StrategySchema
```python
positioning: str           # Brand positioning statement
personality: List[str]     # Brand traits
messaging_framework: Dict  # Key messages
name_options: List[str]    # Brand name ideas
```

### DesignDirectionSchema
```python
keywords: List[str]        # Design keywords
mood: str                  # Design mood/feeling
design_rationale: str      # Design explanation
```

---

## 🔒 Environment Variables

Required in `.env` file:

```env
# LLM - GitHub Models GPT-4o
GITHUB_TOKEN=your_github_token

# Image Generation - Poyo.ai Nano Banana Pro
POYO_API_KEY=your_poyo_key

# Search - Serper for CrewAI
SERPER_API_KEY=your_serper_key
```

---

## 🚀 Production Readiness

### ✅ Implemented
- No mock data - all real APIs
- Structured outputs prevent parsing errors
- Human-in-the-loop approval checkpoints
- Error handling and retries
- Centralized configuration
- Environment-based secrets

### 🔄 Future Enhancements
- Redis for state persistence
- Async/parallel agent execution
- Image download and storage
- Web dashboard for approvals
- Usage tracking and analytics
- Multi-user support

---

## 📈 Performance

### LLM (GitHub GPT-4o)
- Response time: ~2-5 seconds
- Structured output: ~3-7 seconds
- Cost: Free tier available

### Image Generation (Nano Banana Pro)
- Generation time: ~10-30 seconds per image
- Quality: Professional-grade
- Format: 1024x1024 PNG

### Search (Serper)
- Response time: ~1-2 seconds
- Results: 5-10 per query
- Quota: 2,500/month free

---

## 🧪 Testing

Run configuration check:
```bash
python check_config.py
```

Test the full pipeline:
```bash
python main_orchestrator.py
```

---

## 📚 Documentation

- `README.md` - Quick start guide
- `SETUP_GUIDE.md` - Detailed setup instructions
- `TECH_STACK.md` - This file (technical architecture)
- `CREWAI_SUCCESS.md` - CrewAI integration guide
- `IMPROVEMENTS.md` - Change log and improvements

---

**Last Updated**: February 14, 2026  
**Version**: 2.0 (Production Ready)
