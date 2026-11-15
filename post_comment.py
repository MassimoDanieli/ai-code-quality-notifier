import os
import requests

def main():
    github_token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    pr_number = os.getenv("PR_NUMBER")

    if not github_token or not repo or not pr_number:
        raise RuntimeError("Missing GITHUB_TOKEN, GITHUB_REPOSITORY or PR_NUMBER")

    with open("AI_REVIEW.md", "r", encoding="utf-8") as f:
        comment_body = f.read()

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(url, headers=headers, json={"body": comment_body})

    if response.status_code == 201:
        print("✅ Comment posted successfully.")
    else:
        print(f"❌ Failed to post comment: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    main()
