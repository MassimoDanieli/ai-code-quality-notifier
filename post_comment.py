
import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")  # es: MassimoDanieli/ai-code-quality-notifier
PR_NUMBER = os.getenv("PR_NUMBER")

if not GITHUB_TOKEN or not REPO or not PR_NUMBER:
    raise RuntimeError("Missing one or more required environment variables: GITHUB_TOKEN, REPO, PR_NUMBER")

with open("AI_REVIEW.md", "r") as f:
    comment_body = f.read()

api_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

response = requests.post(api_url, headers=headers, json={"body": comment_body})

if response.status_code == 201:
    print("✅ Comment posted successfully.")
else:
    print(f"❌ Failed to post comment: {response.status_code}")
    print(response.json())

# just a quick test    
