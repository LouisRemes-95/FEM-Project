# Stop on first error
$ErrorActionPreference = "Stop"

# Always run from the project directory
Set-Location $PSScriptRoot

# Check that uv is installed
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: uv is not installed."
    Write-Host "Install it from:"
    Write-Host "https://docs.astral.sh/uv/"
    exit 1
}

Write-Host "Setting up project environment..."

# Create/synchronize the virtual environment
# using the exact versions from uv.lock
uv sync --locked

# ===== Make provided files read-only =====

$fileList = @(
    "provided_code",
    "code_to_be_implemented\__init__.py",
    "main.py",
    ".vscode"
)

foreach ($path in $fileList) {
    if (Test-Path $path) {
        if ((Get-Item $path).PSIsContainer) {
            # Folder -> make all contained files read-only
            Get-ChildItem $path -Recurse -File | ForEach-Object {
                $_.Attributes = (
                    $_.Attributes -bor [System.IO.FileAttributes]::ReadOnly
                )
            }
        }
        else {
            # Single file -> make read-only
            $item = Get-Item $path
            $item.Attributes = (
                $item.Attributes -bor [System.IO.FileAttributes]::ReadOnly
            )
        }
    }
    else {
        Write-Warning "Path not found: $path"
    }
}

Write-Host ""
Write-Host "Environment ready."
Write-Host ""
Write-Host "Run the project with:"
Write-Host "    uv run python main.py"
Write-Host ""
Write-Host "Example plotting command:"
Write-Host "    uv run python -m provided_code.plotting input_example --what mesh"