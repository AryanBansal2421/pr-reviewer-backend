import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def quality_agent(diff: str) -> str:
    prompt = f"""You are an expert code quality reviewer. Analyze the following git diff for code quality issues.

Focus on:
- Code readability and clarity
- Variable and function naming conventions
- Code duplication (DRY principle)
- Function length and complexity
- Proper error handling
- Code comments and documentation
- Best practices for the language used

Git Diff:
{diff}

Provide a clear, actionable code quality review. If no issues found, say so.
Format your response as:
✨ CODE QUALITY REVIEW
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