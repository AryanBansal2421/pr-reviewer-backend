import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def architect_agent(diff: str) -> str:
    prompt = f"""You are a senior software architect. Analyze the following git diff for architectural and performance issues.

Focus on:
- Algorithm efficiency and time/space complexity
- Database query optimization
- Unnecessary API calls or network requests
- Memory leaks or resource management issues
- Scalability concerns
- Design pattern violations
- Tight coupling or poor separation of concerns

Git Diff:
{diff}

Provide a clear, actionable architectural review. If no issues found, say so.
Format your response as:
🏗️ ARCHITECTURE REVIEW
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

    return response.json()["choices"][0]["message"]["content"]