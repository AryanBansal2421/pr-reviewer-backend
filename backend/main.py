from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hmac
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="PR Reviewer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "PR Reviewer is running"}

@app.post("/webhook/github")
async def github_webhook(request: Request):
    body = await request.body()
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event", "")

    if event == "pull_request":
        action = payload.get("action", "")
        if action in ["opened", "synchronize"]:
            pr_number = payload["pull_request"]["number"]
            repo_name = payload["repository"]["full_name"]

            # Run review directly (no Celery)
            import asyncio
            from backend.workers.reviewer import run_review
            asyncio.create_task(asyncio.to_thread(run_review, repo_name, pr_number))

            return {"message": f"PR #{pr_number} queued for review"}

    return {"message": "Event ignored"}