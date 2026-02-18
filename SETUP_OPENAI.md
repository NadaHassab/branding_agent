# Quick Setup: Switch to OpenAI API

## Problem
GitHub Models API endpoint (`https://models.github.ai`) is **not accessible** from your network. This is causing connection timeouts.

**Error:** `httpcore.ConnectTimeout: [WinError 10060]`

## Solution
Switch to OpenAI API (more reliable, widely accessible)

---

## Step 1: Get OpenAI API Key

1. Go to: https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

**Note:** OpenAI has a free tier with $5 credit for new accounts. GPT-4o costs approximately $0.005/request for this workload (~$0.10 for full pipeline).

---

## Step 2: Set API Key

### Option A: Environment Variable (Recommended)

**Windows Command Prompt:**
```cmd
set OPENAI_API_KEY=sk-your-key-here
```

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
```

### Option B: Update config.py Directly

Edit `config.py` line 18:
```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-your-actual-key-here")
```

---

## Step 3: Test Connection

```cmd
python test_api_connection.py
```

**Expected output:**
```
================================================================================
LLM API CONNECTIVITY TEST
================================================================================

[CONFIG]
  Provider: openai
  Endpoint: https://api.openai.com/v1
  Model: gpt-4o
  Timeout: 120 seconds

[TEST 1] Initializing LLM client...
[OK] Client initialized

[TEST 2] Sending simple test message...
[OK] Response received in 2.35 seconds
[RESPONSE] OK

[TEST 3] Testing JSON structured output...
[OK] Response received in 1.89 seconds
[RESPONSE] {"status": "success", "message": "API is working"}

================================================================================
[SUCCESS] All tests passed! OPENAI API is working correctly.
================================================================================
```

---

## Step 4: Run Production Pipeline

```cmd
python run_production.py
```

---

## Configuration Details

The system is **already configured** to use OpenAI by default (as of now):

**config.py:**
```python
# Provider Selection (defaults to openai)
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
```

**To switch back to GitHub Models later:**
```cmd
set LLM_PROVIDER=github
```

---

## Troubleshooting

### "API key not configured"
- Check environment variable: `echo %OPENAI_API_KEY%`
- Ensure no typos in the key
- Restart terminal after setting environment variable

### "Authentication failed (401)"
- Verify API key is valid
- Check billing is enabled on OpenAI account
- Ensure key hasn't been revoked

### Still getting timeouts
- Check internet connection
- Try disabling VPN/proxy temporarily
- Verify firewall allows HTTPS to api.openai.com

---

## Alternative: Use Different Provider

If OpenAI is also blocked, you can configure:
- **Anthropic Claude** (via Anthropic API)
- **Azure OpenAI** (via corporate Azure subscription)
- **Local LLM** (Ollama with llama3)

Let me know if you need help configuring an alternative provider.
