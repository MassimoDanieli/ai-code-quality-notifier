
import subprocess
from datetime import datetime, timedelta

DAYS = 7

def get_modified_files(days):
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    cmd = ["git", "log", "--since", since_date, "--name-only", "--pretty=format:"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    files = set(filter(None, result.stdout.splitlines()))
    return files

if __name__ == "__main__":
    files = get_modified_files(DAYS)
    for f in files:
        print(f)
