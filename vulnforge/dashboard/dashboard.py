import json
from pathlib import Path

def build_dashboard(report, output="reports/dashboard.html"):
    Path(output).parent.mkdir(parents=True, exist_ok=True)

    findings = report.get("findings", [])
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
        "INFO": 0,
    }

    for finding in findings:
        severity = str(finding.get("severity", "INFO")).upper()
        summary[severity] = summary.get(severity, 0) + 1

    html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>VulnForge Dashboard</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 40px; background: #f5f5f5; }}
.card {{ background: white; padding: 20px; margin: 10px 0; border-radius: 12px; }}
h1 {{ margin-bottom: 5px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(140px,1fr)); gap: 12px; }}
pre {{ white-space: pre-wrap; }}
</style>
</head>
<body>
<h1>VulnForge</h1>
<p>Security Research & Analysis Platform</p>

<div class="card">
<b>Project:</b> {report.get("project", "Unknown")}<br>
<b>Version:</b> {report.get("version", "Unknown")}<br>
<b>Files:</b> {report.get("file_count", 0)}<br>
<b>Target:</b> {report.get("target", "Local project")}<br>
<b>Risk Score:</b> {report.get("risk_score", 0)}
</div>

<div class="grid">
{''.join(f'<div class="card"><b>{k}</b><br>{v}</div>' for k,v in summary.items())}
</div>

<div class="card">
<h2>Findings</h2>
<pre>{json.dumps(findings, indent=2)}</pre>
</div>

<div class="card">
<b>Made by VYZENTRA</b>
</div>
</body>
</html>"""

    Path(output).write_text(html, encoding="utf-8")
    return output
