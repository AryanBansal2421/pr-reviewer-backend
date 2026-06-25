import os
import requests
from dotenv import load_dotenv

load_dotenv()

r = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/free",
        "messages": [{"role": "user", "content": "say hi"}]
    }
)

print(r.json())