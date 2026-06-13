from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .models import load_csv
from .report import generate_patch_risk_rows, generate_ticket_recommendations

DATA_DIR = Path("data/synthetic")
app = FastAPI(title="EndpointOps 365")


def _summary() -> dict[str, int]:
    devices = load_csv(DATA_DIR / "devices.csv")
    tickets = load_csv(DATA_DIR / "tickets.csv")
    ready = sum(1 for row in devices if row["compliance_state"] == "Compliant")
    return {
        "devices": len(devices),
        "ready": ready,
        "needs_remediation": len(devices) - ready,
        "open_tickets": sum(1 for row in tickets if row["status"] != "Resolved"),
    }


@app.get("/", response_class=HTMLResponse)
def dashboard() -> str:
    summary = _summary()
    return f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>EndpointOps 365</title>
      <style>
        body {{ font-family: system-ui, sans-serif; margin: 2rem; background: #0f172a; color: #e2e8f0; }}
        .grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; }}
        .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1rem; }}
        .value {{ font-size: 2rem; font-weight: 700; }}
        a {{ color: #93c5fd; }}
      </style>
    </head>
    <body>
      <h1>EndpointOps 365</h1>
      <p>Synthetic endpoint lifecycle, readiness, and patch-risk automation lab.</p>
      <section class="grid">
        <div class="card"><div>Devices</div><div class="value">{summary['devices']}</div></div>
        <div class="card"><div>Ready</div><div class="value">{summary['ready']}</div></div>
        <div class="card"><div>Needs remediation</div><div class="value">{summary['needs_remediation']}</div></div>
        <div class="card"><div>Open tickets</div><div class="value">{summary['open_tickets']}</div></div>
      </section>
      <p><a href="/api/patch-risk">Patch risk JSON</a> | <a href="/api/tickets">Ticket JSON</a></p>
    </body>
    </html>
    """


@app.get("/api/summary")
def summary() -> dict[str, int]:
    return _summary()


@app.get("/api/patch-risk")
def patch_risk() -> dict[str, object]:
    items = generate_patch_risk_rows(DATA_DIR)[:10]
    return {"count": len(items), "items": items}


@app.get("/api/tickets")
def tickets() -> dict[str, object]:
    items = generate_ticket_recommendations(DATA_DIR)
    return {"count": len(items), "items": items}
