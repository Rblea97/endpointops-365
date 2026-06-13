from pathlib import Path

from endpointops.report import generate_ticket_recommendations, write_markdown_reports


def test_generate_ticket_recommendations_returns_synthetic_devices():
    tickets = generate_ticket_recommendations(Path("data/synthetic"))
    assert tickets
    assert all(ticket["device_id"].startswith("CML-") for ticket in tickets)
    assert {"ticket_id", "device_id", "severity", "summary", "recommended_action"}.issubset(tickets[0])


def test_write_markdown_reports_creates_expected_files(tmp_path):
    written = write_markdown_reports(Path("data/synthetic"), tmp_path)
    names = {path.name for path in written}
    assert "sample-ticket-output.md" in names
    assert (tmp_path / "sample-ticket-output.md").read_text(encoding="utf-8").startswith("# Ticket Recommendations")
