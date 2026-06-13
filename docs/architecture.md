# Architecture

EndpointOps 365 is intentionally small for the MVP: one repo, one synthetic data set, one report path, and one dashboard.

## Components

| Component | Purpose |
|---|---|
| Synthetic CSV/JSON data | Public-safe devices, users, software, vulnerabilities, tickets, and mock Graph responses |
| Python package | Data validation, sanitizer checks, patch-risk scoring, ticket enrichment, and dashboard API |
| PowerShell scripts | Endpoint readiness checks and Markdown report generation |
| Docker Compose | Reproducible dashboard demo |
| GitHub Actions | Python tests, Pester tests, linting, and security scans |

## Data flow

```text
data/synthetic
  -> endpointops validate-data
  -> PowerShell readiness checks
  -> Python risk scoring
  -> reports/*.md
  -> FastAPI dashboard
```

## Public/private boundary

The public repo uses only synthetic data. Future VM or Entra validation must write raw exports under ignored private folders and publish only sanitized summaries.
