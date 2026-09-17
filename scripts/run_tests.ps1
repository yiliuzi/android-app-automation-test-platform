param(
    [ValidateSet(
        "all",
        "functional",
        "interruption",
        "compatibility"
    )]
    [string]$Suite = "all"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

Write-Host "Project: $ProjectRoot" -ForegroundColor Cyan
Write-Host "Suite: $Suite" -ForegroundColor Cyan

Write-Host "`n[1/5] Checking Android device..." -ForegroundColor Yellow

$DeviceState = adb get-state 2>$null

if ($DeviceState -ne "device") {
    Write-Error (
        "No available Android device was found. " +
        "Start the emulator and run adb devices."
    )
}

adb devices

Write-Host "`n[2/5] Checking Appium server..." -ForegroundColor Yellow

try {
    $null = Invoke-RestMethod `
        -Uri "http://127.0.0.1:4723/status" `
        -Method Get `
        -TimeoutSec 5
} catch {
    Write-Error (
        "Appium server is unavailable at " +
        "http://127.0.0.1:4723. Run appium first."
    )
}

Write-Host "Appium server is available." -ForegroundColor Green

Write-Host "`n[3/5] Running Ruff checks..." -ForegroundColor Yellow

python -m ruff check .

if ($LASTEXITCODE -ne 0) {
    Write-Error "Ruff lint check failed."
}

python -m ruff format --check .

if ($LASTEXITCODE -ne 0) {
    Write-Error "Ruff formatting check failed."
}

Write-Host "Ruff checks passed." -ForegroundColor Green

Write-Host "`n[4/5] Running Pytest..." -ForegroundColor Yellow

$TestTarget = switch ($Suite) {
    "functional" {
        "tests\functional"
    }
    "interruption" {
        "tests\interruption"
    }
    "compatibility" {
        "tests\compatibility"
    }
    default {
        "tests"
    }
}

python -m pytest $TestTarget `
    -v `
    -s `
    --alluredir=reports\allure-results `
    --clean-alluredir

if ($LASTEXITCODE -ne 0) {
    Write-Error "Pytest execution failed."
}

Write-Host "`n[5/5] Generating Allure report..." -ForegroundColor Yellow

$AllureCommand = Get-Command allure -ErrorAction SilentlyContinue

if ($null -eq $AllureCommand) {
    Write-Warning (
        "Allure command was not found. " +
        "Test results are available in reports\allure-results."
    )
} else {
    allure generate `
        reports\allure-results `
        -o reports\allure-report `
        --clean

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Allure report generation failed."
    }

    Write-Host (
        "Allure report: reports\allure-report"
    ) -ForegroundColor Green
}

Write-Host "`nRegression completed successfully." -ForegroundColor Green