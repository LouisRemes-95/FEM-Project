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

# Paths to protect (read + execute only)
$paths = @(
    "provided_code",
    "provided_code\plotting.py",
    "provided_code\solver.py",
    "code_to_be_implemented\__init__.py",
    "main.py",
    ".venv",
    ".vscode"
)

$fileList = @(
    "provided_code",
    "provided_code\plotting.py",
    "provided_code\solver.py",
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
}

Write-Host "`nEnvironment ready. Activate later with:"
Write-Host "`t.venv\Scripts\Activate.ps1"
