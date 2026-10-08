# 🤖 PR Reviewer — Multi-Agent GitHub PR Reviewer

An AI-powered code review system that automatically reviews GitHub Pull Requests using 3 specialized AI agents running in parallel.

## 🔗 Live Demo
- **Dashboard:** https://pr-reviewer-frontend-five.vercel.app
- **Backend API:** https://pr-reviewer-backend-ruig.onrender.com/docs

## 🧠 How It Works

```
GitHub PR opened
      ↓
FastAPI Webhook receives signal
      ↓
3 AI Agents run in parallel
  ├── 🔒 Security Agent
  ├── ✨ Code Quality Agent
  └── 🏗️ Architect Agent
      ↓
Feedback posted as comments on the PR
```

## 🤖 The 3 Agents

| Agent | Role |
|-------|------|
| 🔒 Security Agent | Detects hardcoded secrets, SQL injection, XSS vulnerabilities |
| ✨ Code Quality Agent | Reviews naming conventions, DRY principles, readability |
| 🏗️ Architect Agent | Checks performance, scalability, design patterns |

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python
- **AI:** OpenRouter API (Gemini / free tier models)
- **GitHub Integration:** PyGithub, GitHub Webhooks
- **Async Processing:** Python concurrent.futures (parallel agent execution)
- **Deployment:** Render (backend), Vercel (frontend)
- **Frontend:** Next.js, Tailwind CSS

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/AryanBansal2421/pr-reviewer-backend.git
cd pr-reviewer-backend
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
Create a `.env` file:
```
OPENROUTER_API_KEY=your_openrouter_key
GITHUB_TOKEN=your_github_token
GITHUB_WEBHOOK_SECRET=
```

### 5. Run the server
```bash
uvicorn backend.main:app --reload
```

### 6. Set up GitHub Webhook
- Go to your repo → Settings → Webhooks
- Payload URL: `https://your-backend-url/webhook/github`
- Content type: `application/json`
- Events: Pull requests

## 📁 Project Structure

```
pr-reviewer/
├── backend/
│   ├── agents/
│   │   ├── security_agent.py    # Security vulnerabilities
│   │   ├── quality_agent.py     # Code quality review
│   │   └── architect_agent.py   # Architecture review
│   ├── workers/
│   │   └── reviewer.py          # Parallel agent orchestration
│   ├── api/
│   └── main.py                  # FastAPI app + webhook endpoint
├── requirements.txt
└── .env
```

## ✨ Features

- **Real-time reviews** — triggered automatically on PR open/update
- **Parallel execution** — 3 agents run simultaneously, not sequentially
- **Direct PR comments** — feedback posted line by line on GitHub
- **Free to use** — OpenRouter free tier, no paid API required

## 👨‍💻 Author

**Aryan Bansal** — B.Tech ICE, NSUT Delhi
