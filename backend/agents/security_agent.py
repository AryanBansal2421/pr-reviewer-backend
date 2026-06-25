import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def security_agent(diff: str) -> str:
    prompt = f"""You are an expert security code reviewer. Analyze the following git diff for security vulnerabilities.

Focus on:
- API keys, passwords, tokens, or secrets being hardcoded
- SQL injection vulnerabilities
- XSS vulnerabilities
- Insecure dependencies
- Authentication/authorization issues
- Sensitive data exposure

Git Diff:
{diff}

Provide a clear, actionable security review. If no issues found, say so.
Format your response as:
🔒 SECURITY REVIEW
[Your findings here]
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]