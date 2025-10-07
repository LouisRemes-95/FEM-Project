# Stop on first error
$ErrorActionPreference = "Stop"

# Create virtual environment
python -m venv .venv

# Activate it
& .\.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

Write-Host "Environment ready. Activate later with:"
Write-Host "`t.venv\Scripts\Activate.ps1"

