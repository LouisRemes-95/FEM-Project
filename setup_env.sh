#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v uv >/dev/null 2>&1; then
    echo "❌ uv is not installed."
    echo "Install it from: https://docs.astral.sh/uv/"
    exit 1
fi

echo "Setting up project environment..."
uv sync --locked

echo "Applying file permissions..."
chmod -R 555 provided_code
chmod 444 code_to_be_implemented/__init__.py
chmod 444 main.py
chmod -R 555 .vscode 2>/dev/null || true

echo "✅ Environment ready."
echo "Run the project with:"
echo "uv run python main.py"