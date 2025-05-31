#!/bin/bash

# Imposta variabili
export SMTP_PASSWORD="${SMTP_PASSWORD}"

# Controllo SMTP_PASSWORD
if [ -z "$SMTP_PASSWORD" ]; then
  echo "❌ SMTP_PASSWORD non impostata. Uscita."
  exit 1
fi

# Genera file modificati di recente
echo "📂 File modificati negli ultimi 7 giorni:"
python3 get_recently_modified_files.py

# Esegui analisi principale
echo "🧠 Avvio analisi Sonar report..."
python3 analyze.py
