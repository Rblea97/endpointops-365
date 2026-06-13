from __future__ import annotations

from pathlib import Path

from .models import load_csv
from .scoring import PatchRiskInput, calculate_patch_risk


def _bool(value: str) -> bool:
    return str(value).strip().lower() == "true"


def generate_ticket_recommendations(data_dir: Path) -> list[dict[str, str]]:
    tickets = load_csv(data_dir / "tickets.csv")
    devices = {row["device_id"]: row for row in load_csv(data_dir / "devices.csv")}
    enriched: list[dict[str, str]] = []
    for row in tickets:
        device = devices.get(row["device_id"], {})
        evidence = []
        if device.get("compliance_state") == "NonCompliant":
            evidence.append("device non-compliant")
        if device.get("bitlocker_status") not in ("On", "ExceptionDocumented", None):
            evidence.append(f"BitLocker {device.get('bitlocker_status')}")
        item = dict(row)
        item["evidence"] = "; ".join(evidence) or "synthetic sample ticket"
        enriched.append(item)
    return enriched


def generate_patch_risk_rows(data_dir: Path) -> list[dict[str, str]]:
    software = load_csv(data_dir / "software_inventory.csv")
    vulns = load_csv(data_dir / "vulnerabilities.csv")
    vuln_by_sw = {row["software_name"]: row for row in vulns}
    rows = []
    for item in software:
        vuln = vuln_by_sw.get(item["software_name"])
        if not vuln:
            continue
        risk = calculate_patch_risk(
            PatchRiskInput(
                cvss_base=float(vuln["cvss_base"]),
                epss_percentile=float(vuln["epss_percentile"]),
                known_exploited=_bool(vuln["known_exploited"]),
                asset_criticality=item["asset_criticality"],
                internet_exposed=_bool(item["internet_exposed"]),
                patch_age_bonus=True,
                compensating_control=_bool(item["compensating_control"]),
            )
        )
        rows.append({**item, **vuln, "risk_score": str(risk)})
    return sorted(rows, key=lambda row: int(row["risk_score"]), reverse=True)


def write_markdown_reports(data_dir: Path, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    tickets = generate_ticket_recommendations(data_dir)
    ticket_path = out_dir / "sample-ticket-output.md"
    ticket_lines = ["# Ticket Recommendations", "", "| Ticket | Device | Severity | Action | Evidence |", "|---|---|---|---|---|"]
    for ticket in tickets:
        ticket_lines.append(f"| {ticket['ticket_id']} | {ticket['device_id']} | {ticket['severity']} | {ticket['recommended_action']} | {ticket['evidence']} |")
    ticket_path.write_text("\n".join(ticket_lines) + "\n", encoding="utf-8")

    patch_path = out_dir / "sample-patch-risk-report.md"
    patch_rows = generate_patch_risk_rows(data_dir)[:10]
    patch_lines = ["# Patch Risk Report", "", "| Rank | Device | Software | CVE | Risk | Recommended action |", "|---:|---|---|---|---:|---|"]
    for index, row in enumerate(patch_rows, start=1):
        patch_lines.append(f"| {index} | {row['device_id']} | {row['software_name']} | {row['cve_id']} | {row['risk_score']} | Update to {row['fixed_version']} |")
    patch_path.write_text("\n".join(patch_lines) + "\n", encoding="utf-8")
    return [ticket_path, patch_path]
