#!/bin/bash

# Controlla API key e token
if [ -z "$SMTP_PASSWORD" ]; then
  echo "❌ SMTP_PASSWORD non impostata"
  exit 1
fi

if [ -z "$OPENAI_API_KEY" ]; then
  echo "❌ OPENAI_API_KEY non impostata"
  exit 1
fi

# Esegui analisi code smells
echo "🚨 Code Smell Analyzer (SonarQube JSON)"
python3 analyze.py

# Esegui analisi semantica con GPT
echo "🧠 Semantic Code Review via GPT-4"
python3 semantic_reviewer.py

# Se in PR, posta il commento
if [ "$GITHUB_TOKEN" != "" ] && [ "$PR_NUMBER" != "" ] && [ "$GITHUB_REPOSITORY" != "" ]; then
  echo "💬 Posto commento su PR #$PR_NUMBER"
  python3 post_comment.py
else
  echo "ℹ️ Skip commento su PR (non in contesto PR o variabili mancanti)"
fi
