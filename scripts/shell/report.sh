#!/usr/bin/env bash
set -euo pipefail
python -m endpointops.cli generate-reports --data-dir data/synthetic --out-dir reports
pwsh -NoProfile -File ./scripts/powershell/New-EndpointReadinessReport.ps1 -DeviceCsv ./data/synthetic/devices.csv -OutputPath ./reports/sample-endpoint-readiness-report.md -Now '2026-06-13'
pwsh -NoProfile -File ./scripts/powershell/New-PatchRiskReport.ps1 -DeviceCsv ./data/synthetic/devices.csv -SoftwareCsv ./data/synthetic/software_inventory.csv -VulnerabilityCsv ./data/synthetic/vulnerabilities.csv -OutputPath ./reports/sample-patch-risk-report.md
