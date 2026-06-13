# Demo Script

## Goal

Show how EndpointOps 365 turns a synthetic laptop batch into readiness, patch-risk, and ticket outputs.

## Walkthrough

1. Explain that all data is synthetic and public-safe.
2. Show `data/synthetic/devices.csv` with 25 fake endpoints.
3. Run `make test` to prove Python and PowerShell checks pass.
4. Run `make report` to regenerate Markdown reports.
5. Open `reports/sample-endpoint-readiness-report.md` and point out one ready endpoint and one remediation case.
6. Open `reports/sample-patch-risk-report.md` and show the prioritized patch queue.
7. Start the dashboard with `docker compose up --build`.
8. Open `http://localhost:8000`.
9. Show gitleaks/Trivy via `make scan`.
10. Explain that real VM/Entra validation is a later private phase with sanitized public evidence only.
