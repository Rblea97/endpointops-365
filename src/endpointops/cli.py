from __future__ import annotations

import argparse
from pathlib import Path

from .models import load_csv, validate_required_columns
from .report import write_markdown_reports
from .sanitizer import scan_path_for_public_safety

REQUIRED = {
    "devices.csv": ["device_id", "asset_tag", "serial_number", "device_role", "bios_mode", "secure_boot"],
    "users.csv": ["user_id", "display_name", "user_principal_name"],
    "software_inventory.csv": ["device_id", "software_name", "installed_version"],
    "vulnerabilities.csv": ["vuln_id", "cve_id", "software_name", "cvss_base", "epss_percentile"],
    "tickets.csv": ["ticket_id", "device_id", "severity", "recommended_action"],
}


def validate_data(data_dir: Path) -> int:
    errors: list[str] = []
    for filename, fields in REQUIRED.items():
        errors.extend(f"{filename}: {error}" for error in validate_required_columns(load_csv(data_dir / filename), fields))
    errors.extend(scan_path_for_public_safety(data_dir))
    if errors:
        print("Data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Data validation passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="endpointops")
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate-data")
    v.add_argument("--data-dir", type=Path, default=Path("data/synthetic"))
    r = sub.add_parser("generate-reports")
    r.add_argument("--data-dir", type=Path, default=Path("data/synthetic"))
    r.add_argument("--out-dir", type=Path, default=Path("reports"))
    args = parser.parse_args(argv)
    if args.command == "validate-data":
        return validate_data(args.data_dir)
    if args.command == "generate-reports":
        written = write_markdown_reports(args.data_dir, args.out_dir)
        for path in written:
            print(path)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
