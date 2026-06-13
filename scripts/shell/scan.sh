#!/usr/bin/env bash
set -euo pipefail
gitleaks detect --source . --config tools/gitleaks.toml --no-banner
trivy fs --config tools/trivy.yaml .
