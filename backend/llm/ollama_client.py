import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")

def generate_response(prompt):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={"model": "llama3", "prompt": prompt}
    )
    response.raise_for_status()
    return response.json()["response"]

