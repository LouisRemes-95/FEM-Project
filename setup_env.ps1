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

# Apply Read + Execute permissions for Everyone
foreach ($path in $paths) {
    if (Test-Path $path) {
        $acl = Get-Acl $path
        $acl.SetAccessRuleProtection($true, $false)  # Disable inheritance
        $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "ReadAndExecute", "Allow")
        $acl.SetAccessRule($rule)
        Set-Acl $path $acl
        Write-Host "Set Read+Execute only for $path"
    } else {
        Write-Warning "Path not found: $path"
    }
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
