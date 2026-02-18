# Setup Guide for Brand Agent System

## 🔑 Required API Keys

### 1. GitHub Token (Already Configured ✅)
Your GitHub token is already set in `.env`

### 2. Poyo.ai API Key (Already Configured ✅)
Your Poyo.ai API key is already set in `.env`

### 3. Serper API Key (REQUIRED - Get Free Key)

**CrewAI uses Serper.dev for search functionality. You need to get a free API key:**

#### Steps to Get Serper API Key:

1. **Visit Serper.dev**
   - Go to: https://serper.dev/

2. **Sign Up**
   - Click "Sign Up" or "Get Started"
   - Sign up with Google or Email
   - It's FREE with 2,500 free searches

3. **Get Your API Key**
   - After signing in, go to your dashboard
   - Copy your API key

4. **Add to .env File**
   - Open `.env` file in this directory
   - Replace `your_serper_api_key_here` with your actual key:
   ```
   SERPER_API_KEY=your_actual_key_here
   ```

## 📦 Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**:
   ```bash
   python -c "import crewai; print('CrewAI installed successfully')"
   ```

## 🚀 Running the Application

### Option 1: Command Line Test
```bash
python main_orchestrator.py
```

### Option 2: Web Interface (Coming Soon)
```bash
python web_app.py
```

## 🔍 What CrewAI Search Does

- **Market Competitor Analysis**: Searches for top competitors in any industry
- **Audience Profiling**: Finds consumer behavior trends and insights
- **More Reliable**: Enterprise-grade search API vs free DuckDuckGo
- **Better Results**: Structured data with higher quality results

## ⚠️ Troubleshooting

### "SERPER_API_KEY not set" Error
- Make sure you added the key to `.env` file
- Restart the application after adding the key

### Search Not Working
- Verify your API key is correct
- Check you haven't exceeded the free tier limit (2,500 searches/month)
- Visit https://serper.dev/dashboard to check your usage

## 💡 Alternative: Test Without Search

If you want to test the system without setting up search immediately, you can create a mock mode (contact developer for this option).

## 📧 Need Help?

If you encounter issues:
1. Check all API keys are properly set in `.env`
2. Verify internet connection
3. Check Serper.dev dashboard for any issues with your account
