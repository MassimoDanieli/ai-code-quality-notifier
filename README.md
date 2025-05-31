
# 🧠 AI Code Quality Notifier – Minimal PoC

Questo è un prototipo che analizza i risultati di SonarQube per identificare *code smells critici o blocker* in file modificati di recente, e invia una notifica via **email Gmail SMTP** se la soglia viene superata.

## 📦 Contenuto del progetto

- `analyze.py` – Analizza un report JSON di SonarQube e invia un'email se serve
- `get_recently_modified_files.py` – Trova i file modificati negli ultimi 7 giorni con `git log`
- `sonar_report.json` – Esempio di report SonarQube
- `run.sh` – Script per eseguire tutto in un colpo solo

## 🚀 Come si usa

### 1. Clona o scarica il progetto

```bash
git clone ...
cd ...
```

### 2. Esporta la tua Gmail App Password

```bash
export SMTP_PASSWORD="la-tua-app-password-gmail"
```

> ⚠️ Devi prima generare una App Password da https://myaccount.google.com/apppasswords

### 3. Assicurati di essere in una repo Git con commit recenti

```bash
git status
```

### 4. Lancia il sistema

```bash
bash run.sh
```

## ✅ Requisiti

- Python 3.10+
- Una repo Git
- Report `sonar_report.json`
- Gmail App Password

## 📧 Email di esempio

```
🚨 AI Quality Gate Triggered

Detected 2 critical code smells in files modified in the last 7 days:

• src/db/dao.py — "Refactor this function to reduce its Cognitive Complexity..."
• src/utils/legacy_parser.py — "Replace this usage of System.out or System.err..."

Recommended action: consider refactoring or improving coverage.
```

---

## 📌 Roadmap futura

- Estensione a Slack, GitHub Comment, Jira
- Parsing automatico da API SonarQube
- Refactoring assistito via LLM (CodeLlama, GPT-4)
