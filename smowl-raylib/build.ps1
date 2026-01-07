# build.ps1
$ErrorActionPreference = "Stop"

Write-Host "Checking build environment..." -ForegroundColor Cyan

# 1. Check for CMake and add to PATH if missing
if (-not (Get-Command cmake -ErrorAction SilentlyContinue)) {
    $cmakePath = "C:\Program Files\CMake\bin"
    if (Test-Path $cmakePath) {
        $env:PATH = "$cmakePath;$env:PATH"
        Write-Host "Found CMake at default location. Added to session PATH." -ForegroundColor Gray
    } else {
        Write-Warning "CMake not found in PATH or standard location. Build may fail."
    }
}

# 2. Check for Ninja and add to PATH if missing
if (-not (Get-Command ninja -ErrorAction SilentlyContinue)) {
    Write-Host "Ninja not in PATH. Searching WinGet packages..." -ForegroundColor Gray
    
    # Search for ninja.exe in the local app data WinGet packages
    $ninjaExe = Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages" -Recurse -Filter "ninja.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
    
    if ($ninjaExe) {
        $ninjaDir = $ninjaExe.DirectoryName
        $env:PATH = "$ninjaDir;$env:PATH"
        Write-Host "Found Ninja at: $ninjaDir" -ForegroundColor Gray
        Write-Host "Added to session PATH." -ForegroundColor Gray
    } else {
        Write-Error "Ninja not found. Please ensure it is installed (winget install Ninja-build.Ninja) or restart your terminal."
    }
}

# 3. Configure
Write-Host "`n[1/2] Configuring project..." -ForegroundColor Cyan
cmake -G "Ninja" -B build -S .

# 4. Build
Write-Host "`n[2/2] Compiling..." -ForegroundColor Cyan
cmake --build build

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nBuild Success! Run the app with:" -ForegroundColor Green
    Write-Host ".\build\smowl-raylib.exe" -ForegroundColor White
} else {
    Write-Error "Build failed."
}
