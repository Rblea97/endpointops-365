from __future__ import annotations

import re
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+)")
BITLOCKER_KEY_RE = re.compile(r"\b(?:\d{6}-){7}\d{6}\b")
PRIVATE_HINTS = ("tenant-exports", "hardware-hashes", "bitlocker-exports")


def scan_path_for_public_safety(path: Path) -> list[str]:
    findings: list[str] = []
    files = [path] if path.is_file() else [p for p in path.rglob("*") if p.is_file()]
    for file_path in files:
        rel = str(file_path)
        if any(hint in rel.lower() for hint in PRIVATE_HINTS):
            findings.append(f"{rel}: private export path name")
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            findings.append(f"{rel}: unreadable file: {exc}")
            continue
        if BITLOCKER_KEY_RE.search(text):
            findings.append(f"{rel}: possible BitLocker recovery key")
        for match in EMAIL_RE.finditer(text):
            domain = match.group(1).lower()
            if not domain.endswith(".example"):
                findings.append(f"{rel}: non-example email domain: {domain}")
    return findings
