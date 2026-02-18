# Brand Agent System 🚀

AI-powered brand strategy and identity system using **GitHub GPT-4o**, **Poyo.ai Nano Banana Pro**, and **CrewAI**.

## ⚡ Quick Start

### 1. Verify Setup
```bash
python check_config.py
```
**Expected**: ✅ All 3 API keys configured

### 2. Run
```bash
python main_orchestrator.py
```

### 3. Check Output
Look in `output/` folder for generated files

---

## 🤖 Technology

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | GitHub GPT-4o | Strategy & Analysis |
| **Images** | Poyo.ai Nano Banana Pro | Logo Generation |
| **Search** | CrewAI + Serper | Market Research |

---

## 📚 Documentation

- **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** ⭐ **START HERE** - Complete system overview
- **[TECH_STACK.md](TECH_STACK.md)** - Technical architecture
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions

---

## ✨ Key Features

- ✅ **No Mock Data** - All real APIs (GitHub GPT-4o, Poyo.ai, Serper)
- ✅ **Structured Outputs** - Pydantic schemas prevent errors
- ✅ **Human-in-the-Loop** - Approval checkpoints before design
- ✅ **Production Ready** - Fully configured and tested

---

## 🏗️ How It Works

```
User Brief → Research Agent → Strategy Agent → ⏸️ Approval → Design Agent → Deliverables
              (CrewAI)         (GPT-4o)                      (Nano Banana)    (PDF/DOCX)
```

**1. Research** (CrewAI + Serper): Market analysis, competitor research  
**2. Strategy** (GPT-4o): Brand positioning, personality, messaging  
**3. ⏸️ Approval**: Human review before design  
**4. Design** (Nano Banana Pro): Logo concepts, color palette  
**5. Deliverables**: Professional PDFs and documents

---

## 🔧 Configuration Status

Run `python check_config.py` to verify:

- ✅ GitHub Token (GPT-4o LLM)
- ✅ Poyo.ai API Key (Nano Banana Pro)
- ✅ Serper API Key (CrewAI Search)

All API keys are **already configured** in your `.env` file.

---

## 📊 Sample Output

**For**: Sustainable Coffee Shop  
**Industry**: Food & Beverage  
**Generates**:
- Market analysis with competitor insights
- Brand positioning statement
- 3-5 personality traits
- Messaging framework
- 3 logo concepts (AI-generated)
- Color palette
- Typography recommendations
- Professional PDF/DOCX reports

---

## 🚀 Running the System

### Default Test Run
```bash
python main_orchestrator.py
```
Uses sample company: "EcoFresh" (sustainable food delivery)

### Custom Company
Edit lines 50-57 in `main_orchestrator.py`:
```python
initial_brief: ClientBrief = {
    "company_name": "Your Company",
    "industry": "Your Industry",
    "target_audience": "Your Audience",
    # ... etc
}
```

---

## 📁 Project Structure

```
brand_agent/
├── config.py              # ⚙️ All configuration (GPT-4o, Nano Banana, Serper)
├── main_orchestrator.py   # 🚀 Main entry point
├── agents/                # 🤖 AI Agents (Research, Strategy, Design)
├── tools/                 # 🔧 CrewAI search, Poyo.ai images, documents
├── output/                # 📦 Generated deliverables
└── .env                   # 🔑 API keys (✅ configured)
```

---

## 🧪 Testing

All components tested and working:
- ✅ GitHub GPT-4o integration
- ✅ Poyo.ai Nano Banana Pro integration
- ✅ CrewAI + Serper search
- ✅ Pydantic structured outputs
- ✅ Human-in-the-loop approvals

---

## 📖 Learn More

Read the complete documentation:
1. **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - Comprehensive guide
2. **[TECH_STACK.md](TECH_STACK.md)** - Architecture details
3. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Setup walkthrough

---

**Status**: ✅ Production Ready  
**Version**: 2.0  
**Last Updated**: February 14, 2026

## 📂 Project Structure

- `agents/`: Contains the logic for each specific agent.
- `tools/`: Helper functions for research, design generation, and file creation.
- `state.py`: Defines the shared state schema tailored for branding.
- `config.py`: Configuration settings.
- `output/`: Generated deliverables will appear here.

## 🧩 Customization

- **Modify the Client Brief**: Edit the `initial_brief` dictionary in `main_orchestrator.py` to change the input brand parameters.
- **Swap Models**: Change the LLM models in `config.py` or within individual agent files.
