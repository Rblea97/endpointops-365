#!/usr/bin/env bash
set -euo pipefail
python -m pytest tests/python -q
pwsh -NoProfile -Command "Invoke-Pester ./tests/powershell -CI"
