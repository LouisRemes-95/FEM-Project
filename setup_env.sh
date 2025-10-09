#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
chmod -R 555 provided_code code_to_be_implemented/__init__.py main.py .venv .vscode
rm requirements.txt setup_env.ps1 setup_env.sh .gitignore
echo "✅ Environment ready. Activate with: source .venv/bin/activate"
