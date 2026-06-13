.PHONY: setup seed test lint report scan demo clean

PYTHON ?= python
DATA_DIR ?= data/synthetic
REPORT_DIR ?= reports

setup:
	$(PYTHON) -m pip install -e ".[dev]"

seed:
	$(PYTHON) -m endpointops.cli validate-data --data-dir $(DATA_DIR)

test:
	$(PYTHON) -m pytest tests/python -q
	pwsh -NoProfile -Command "Invoke-Pester ./tests/powershell -CI"

lint:
	pwsh -NoProfile -Command "Invoke-ScriptAnalyzer -Path ./scripts/powershell -Recurse -Severity Warning,Error"

report:
	$(PYTHON) -m endpointops.cli generate-reports --data-dir $(DATA_DIR) --out-dir $(REPORT_DIR)
	pwsh -NoProfile -File ./scripts/powershell/New-EndpointReadinessReport.ps1 -DeviceCsv ./data/synthetic/devices.csv -OutputPath ./reports/sample-endpoint-readiness-report.md -Now '2026-06-13'
	pwsh -NoProfile -File ./scripts/powershell/New-PatchRiskReport.ps1 -DeviceCsv ./data/synthetic/devices.csv -SoftwareCsv ./data/synthetic/software_inventory.csv -VulnerabilityCsv ./data/synthetic/vulnerabilities.csv -OutputPath ./reports/sample-patch-risk-report.md

scan:
	gitleaks detect --source . --config tools/gitleaks.toml --no-banner
	trivy fs --config tools/trivy.yaml .

demo:
	docker compose up --build

clean:
	rm -rf .pytest_cache build dist *.egg-info
