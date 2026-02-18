# 🚀 Brand Agent Web Application - Quick Start Guide

## Overview
This is a production-ready web interface for the Brand Agent System. It provides an intuitive UI for creating AI-powered brand strategies with human-in-the-loop approval.

## Features
✨ **Beautiful Web Interface** - Modern, responsive design
🔄 **Real-time Progress** - Live updates as agents work
⏸️ **Human Approval** - Review and approve strategy before design
📥 **Downloadable Deliverables** - Get DOCX and PDF files
🎨 **Visual Feedback** - See all outputs in a clean format

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Make sure your `.env` file has the required API keys:
```env
GITHUB_TOKEN=your_github_token_here
POYO_API_KEY=your_poyo_api_key_here
```

### 3. Run the Web App
```bash
python run_web.py
```

Or directly:
```bash
python web_app.py
```

### 4. Open Your Browser
Navigate to: **http://localhost:5000**

## Usage Flow

### Step 1: Fill Out Brand Brief
Enter your brand information:
- Company Name
- Industry
- Target Audience
- Brand Type (New/Rebrand)
- Budget Tier
- Core Values
- Mission Statement

### Step 2: Monitor Progress
Watch as the AI agents work through:
1. 🕵️ **Research Phase** - Market and competitor analysis
2. 🧠 **Strategy Phase** - Brand positioning and messaging
3. 🎨 **Design Phase** - Visual identity creation
4. 📦 **Deliverables** - Document generation

### Step 3: Review & Approve Strategy
When the strategy is ready:
- Review the generated positioning, personality, and messaging
- Click "Approve Strategy & Continue to Design"
- The workflow will continue to the design phase

### Step 4: Download Results
Once complete, download:
- 📄 Brand Strategy Document (DOCX)
- 📋 Brand Guidelines (PDF)

## API Endpoints

### `GET /`
Main page with brand brief form

### `POST /start_workflow`
Start a new brand creation workflow
- **Body**: JSON with client brief data
- **Returns**: Workflow ID

### `GET /workflow_status/<workflow_id>`
Get current status of a workflow
- **Returns**: Status, outputs, and progress

### `POST /approve_strategy/<workflow_id>`
Approve strategy and continue to design
- **Returns**: Success confirmation

### `GET /workflow/<workflow_id>`
Workflow progress page with live updates

### `GET /download/<workflow_id>/<file_type>`
Download deliverables
- **file_type**: `strategy` or `guidelines`

## Project Structure
```
brand_agent/
├── web_app.py              # Flask application
├── run_web.py              # Quick start script
├── templates/
│   ├── index.html          # Main form page
│   └── workflow.html       # Progress page
├── static/
│   └── style.css           # Styling
├── agents/                 # AI agents
├── tools/                  # Research & design tools
├── output/                 # Generated files
└── .env                    # API keys
```

## Production Deployment

### Using Gunicorn (Recommended)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```

### Using Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "web_app:app"]
```

### Environment Variables for Production
```env
FLASK_ENV=production
GITHUB_TOKEN=your_token
POYO_API_KEY=your_key
```

## Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill
```

### Missing Dependencies
```bash
pip install -r requirements.txt --upgrade
```

### API Key Issues
Check that `.env` file has valid keys:
```bash
cat .env  # Linux/Mac
type .env  # Windows
```

## Features in Detail

### Real-time Updates
The workflow page polls the server every 2 seconds for status updates, providing live feedback on agent progress.

### State Management
Uses LangGraph's MemorySaver for checkpoint/resume functionality. Each workflow has a unique ID for tracking.

### Error Handling
- Network errors are caught and displayed
- API failures show user-friendly messages
- Workflows can be retried from the home page

### Responsive Design
Works on desktop, tablet, and mobile devices with adaptive layouts.

## Security Notes

⚠️ **For Production:**
- Change the Flask secret key in `web_app.py`
- Use HTTPS (SSL/TLS)
- Implement authentication
- Use a production WSGI server (Gunicorn/uWSGI)
- Store API keys securely (e.g., AWS Secrets Manager)
- Use a proper database instead of in-memory storage

## Support

For issues or questions:
1. Check the console logs in the browser
2. Check the terminal logs where the Flask server is running
3. Verify API keys are valid
4. Ensure internet connection for research tools

## Next Steps

Consider adding:
- User authentication
- Database for persistent storage
- Email notifications when workflows complete
- More customization options
- Batch processing
- API rate limiting
- Caching for better performance
