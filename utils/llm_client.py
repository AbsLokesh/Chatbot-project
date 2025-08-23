import os
import requests
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")

def anthropic_chat(messages, stream=False):
    """
    Calls Anthropic API with a list of messages in format:
    [{"role": "user", "content": "Hello"}]
    """
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_KEY,
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01"
    }

    data = {
        "model": "claude-3-5-sonnet-20240620",
        "messages": messages,
        "max_tokens": 512,
        "stream": stream
    }

    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code != 200:
        return f"Error: {resp.text}"

    return resp.json()["content"][0]["text"]
