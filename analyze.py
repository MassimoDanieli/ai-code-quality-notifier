
import os
import json
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurazione
THRESHOLD_BLOCKERS = 2
MODIFIED_DAYS_LIMIT = 7
EMAIL_FROM = "massimo.danieli@gmail.com"
EMAIL_TO = "massimo.danieli@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Carica il report di SonarQube
with open("sonar_report.json") as f:
    report = json.load(f)

def filter_issues(report):
    issues = report.get("issues", [])
    return [
        i for i in issues
        if i.get("type") == "CODE_SMELL" and i.get("severity") in ("BLOCKER", "CRITICAL")
    ]

def get_recently_modified_files():
    # Mock: in uno scenario reale, usa git log per i file modificati negli ultimi X giorni
    return {"src/db/dao.py", "src/utils/legacy_parser.py"}

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    password = os.environ.get("SMTP_PASSWORD")
    if not password:
        raise RuntimeError("SMTP_PASSWORD env var not set")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, password)
        server.send_message(msg)

# Main
issues = filter_issues(report)
files = set(i.get("component", "").replace("project_key:", "") for i in issues)
recent_files = get_recently_modified_files()
target_files = files.intersection(recent_files)

if issues and target_files and len(issues) >= THRESHOLD_BLOCKERS:
    body = f"🚨 AI Quality Gate Triggered\n\nDetected {len(issues)} critical code smells in files modified in the last {MODIFIED_DAYS_LIMIT} days:\n\n"
    for issue in issues:
        path = issue.get("component", "unknown").replace("project_key:", "")
        message = issue.get("message", "No description")
        body += f"• {path} — \"{message}\"\n"
    body += "\nRecommended action: consider refactoring or improving coverage."
    send_email("🚨 AI Quality Alert: Code Quality Issues Detected", body)
else:
    print("No significant issues found or threshold not reached.")
