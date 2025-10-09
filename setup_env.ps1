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

# ===== Add permission settings and cleanup below =====

$fileList = @(
    "provided_code",
    "code_to_be_implemented\__init__.py",
    "main.py",
    ".venv",
    ".vscode"
)

foreach ($path in $fileList) {
    if (Test-Path $path) {
        if ((Get-Item $path).PSIsContainer) {
            Get-ChildItem $path -Recurse -File | ForEach-Object {
                $_.Attributes = ($_.Attributes -band -bnot [System.IO.FileAttributes]::ReadOnly)
            }
        } else {
            $item = Get-Item $path
            $item.Attributes = ($item.Attributes -band -bnot [System.IO.FileAttributes]::ReadOnly)
        }
    } else {
        Write-Warning "Path not found: $path"
    }

# Remove setup-related files
$removeFiles = @("requirements.txt", "setup_env.ps1", "setup_env.sh", ".gitignore")
foreach ($file in $removeFiles) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "Removed $file"
    }
}

Write-Host "`nEnvironment ready. Activate later with:"
Write-Host "`t.venv\Scripts\Activate.ps1"
