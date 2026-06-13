from pathlib import Path

from endpointops.models import load_csv, validate_required_columns


def test_load_csv_reads_synthetic_devices():
    rows = load_csv(Path("data/synthetic/devices.csv"))
    assert len(rows) == 25
    assert rows[0]["device_id"] == "CML-LT-001"


def test_validate_required_columns_rejects_missing_field():
    rows = [{"device_id": "CML-LT-001"}]
    errors = validate_required_columns(rows, ["device_id", "asset_tag"])
    assert errors == ["row 1 missing required field: asset_tag"]
