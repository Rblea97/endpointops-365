# EndpointOps 365

EndpointOps 365 is a public-safe endpoint operations portfolio lab. It simulates a Windows endpoint lifecycle workflow with synthetic devices, users, software inventory, vulnerabilities, tickets, readiness checks, patch-risk scoring, reports, and a small dashboard.

## What this project demonstrates

- Endpoint lifecycle support automation
- Windows readiness validation logic
- Intune/M365/Entra readiness concepts through mock data and dry-run scripts
- Patch and vulnerability triage
- Ticket and runbook generation
- CI/CD and security scanning

## Why I built it

This project turns hands-on endpoint support work into a safe public artifact: laptop intake, validation, patch review, loaner handling, compliance reporting, and operational documentation without exposing employer or tenant data.

## Security and privacy

This repository contains only synthetic data. It does not contain employer data, real tenant IDs, real users, real devices, real serial numbers, real tickets, real BitLocker keys, hardware hashes, app secrets, or production screenshots.

See `SECURITY.md` and `docs/privacy-and-sanitization.md`.

## Architecture

```text
Synthetic CSV/JSON
  -> validation and sanitizer checks
  -> PowerShell endpoint readiness checks
  -> Python patch-risk scoring and ticket enrichment
  -> Markdown reports and FastAPI dashboard
  -> tests, gitleaks, Trivy, and CI
```

## Quickstart

```bash
python -m pip install -e ".[dev]"
make test
make report
make scan
docker compose up --build
```

Open <http://localhost:8000> for the dashboard.

## Reports

- `reports/sample-endpoint-readiness-report.md`
- `reports/sample-patch-risk-report.md`
- `reports/sample-ticket-output.md`

## Scripts

- `scripts/powershell/Invoke-EndpointReadinessCheck.ps1`
- `scripts/powershell/New-EndpointReadinessReport.ps1`
- `scripts/powershell/New-PatchRiskReport.ps1`
- `scripts/powershell/Invoke-GraphDryRun.ps1`

## Limitations

The MVP is offline and synthetic. Real Windows VM validation, Graph read-only validation, and Intune tenant integration are later phases and must keep raw exports private.
