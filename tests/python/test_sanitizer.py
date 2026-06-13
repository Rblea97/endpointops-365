from pathlib import Path

from endpointops.sanitizer import scan_path_for_public_safety


def test_sanitizer_accepts_synthetic_data():
    findings = scan_path_for_public_safety(Path("data/synthetic"))
    assert findings == []


def test_sanitizer_flags_real_email_domain(tmp_path):
    sample = tmp_path / "unsafe.csv"
    sample.write_text("user,email\nExample,person@gmail.com\n", encoding="utf-8")
    findings = scan_path_for_public_safety(tmp_path)
    assert any("non-example email domain" in finding for finding in findings)


def test_sanitizer_flags_bitlocker_recovery_key(tmp_path):
    sample = tmp_path / "unsafe.txt"
    sample.write_text("111111-222222-333333-444444-555555-666666-777777-888888", encoding="utf-8")
    findings = scan_path_for_public_safety(tmp_path)
    assert any("possible BitLocker recovery key" in finding for finding in findings)
