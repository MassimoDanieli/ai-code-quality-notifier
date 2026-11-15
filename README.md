> [!WARNING]
> **Progetto archiviato (novembre 2026).** Questo prototipo del 2025 chiamava `gpt-4`, che OpenAI ha spento il 23 ottobre 2026: non funziona più.
> Le sue funzioni ora vivono in **[ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit)**: triage delle issue SonarQube BLOCKER/CRITICAL nei file cambiati di recente, con fix proposti e commento sulla PR (`aikit sonar` / workflow `ai-sonar-triage.yml`), con qualsiasi fornitore (Anthropic, OpenAI o un modello locale).
>
> *Archived (November 2026): this 2025 prototype called `gpt-4`, shut down by OpenAI on 23 October 2026. Its features live on in [ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit) (`aikit sonar`).*


# 🤖 AI Code Quality Notifier

[![AI Quality Notifier](https://github.com/MassimoDanieli/ai-code-quality-notifier/actions/workflows/quality-check.yml/badge.svg)](https://github.com/MassimoDanieli/ai-code-quality-notifier/actions)

Questo è un **prototipo intelligente** per migliorare la qualità del codice nelle pipeline CI/CD.  
Analizza i report di **SonarQube**, individua *code smells critici o blocker* in file modificati di recente, e invia una **notifica via email (SMTP Gmail)** se necessario.

---

## 🚀 Come funziona

1. Legge il file `sonar_report.json`
2. Filtra solo problemi `BLOCKER` e `CRITICAL`
3. Controlla se i file coinvolti sono stati modificati negli ultimi 7 giorni
4. Se la soglia è superata, **manda una mail con dettagli**
5. Funziona anche in **GitHub Actions** con `SMTP_PASSWORD` salvata come secret

---

## 📦 Struttura del progetto

```
.
├── run.sh                      # Script per eseguire tutto
├── sonar_report.json          # Report SonarQube di esempio
├── src/
│   ├── analyze.py             # Analisi e invio email
│   └── get_recently_modified_files.py  # Estrae file toccati da git
├── .github/workflows/
│   └── quality-check.yml      # GitHub Actions CI
```

---

## ⚙️ Setup rapido

```bash
export SMTP_PASSWORD="la-tua-app-password"
bash run.sh
```

## 🔐 GitHub Actions Secrets

Aggiungi il secret `SMTP_PASSWORD` su  
`https://github.com/MassimoDanieli/ai-code-quality-notifier/settings/secrets/actions`

---

## 📧 Esempio Email

```
🚨 AI Quality Gate Triggered

Detected 2 critical code smells in files modified in the last 7 days:

• src/db/dao.py — "Cognitive complexity too high"
• src/utils/legacy_parser.py — "Use logger instead of print"

Recommended action: refactor before merge.
```

---

## 📌 Prossimi step

- Integrazione con Slack, GitHub PR comments, Jira
- Refactoring automatico via LLM
- Dashboard di osservabilità

---

## 🧠 Licenza

MIT — Made with ❤️ by [Massimo Danieli](https://github.com/MassimoDanieli)
