from html import escape
from pathlib import Path

from vulnforge.plugins.base import Finding


class HTMLReporter:
    name = "HTML Reporter"

    def write(self, findings: list[Finding], output: str = "reports/report.html") -> Path:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        summary = {level: sum(1 for f in findings if f.severity.upper() == level) for level in ["INFO","LOW","MEDIUM","HIGH","CRITICAL"]}

        rows = "".join(
            f"""
            <tr>
                <td><code>{escape(f.finding_id)}</code></td>
                <td>{escape(f.severity)}</td>
                <td>{escape(f.title)}</td>
                <td>{escape(f.description)}</td>
                <td>{escape(f.remediation)}</td>
                <td>{escape(f.confidence)}</td>
            </tr>
            """
            for f in findings
        )

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VulnForge Security Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    background: #f4f4f4;
    color: #222;
}}
header {{
    background: #111;
    color: #fff;
    padding: 25px;
    border-radius: 12px;
}}
table {{
    width: 100%;
    margin-top: 25px;
    border-collapse: collapse;
    background: #fff;
}}
th, td {{
    padding: 12px;
    border: 1px solid #ddd;
    text-align: left;
    vertical-align: top;
}}
th {{
    background: #222;
    color: #fff;
}}
code {{
    font-size: 12px;
}}
footer {{
    margin-top: 30px;
    text-align: center;
    color: #666;
}}
</style>
</head>
<body>

<header>
<h1>VulnForge Security Report</h1>
<p>Security Research & Analysis Platform</p>
<p>Findings: {len(findings)}</p>
<p>INFO: {summary["INFO"]} | LOW: {summary["LOW"]} | MEDIUM: {summary["MEDIUM"]} | HIGH: {summary["HIGH"]} | CRITICAL: {summary["CRITICAL"]}</p>
</header>

<table>
<thead>
<tr>
<th>ID</th>
<th>Severity</th>
<th>Finding</th>
<th>Description</th>
<th>Remediation</th>
<th>Confidence</th>
</tr>
</thead>
<tbody>
{rows}
</tbody>
</table>

<footer>
Made by VYZENTRA · VulnForge 0.1.0
</footer>

</body>
</html>
"""

        path.write_text(html, encoding="utf-8")
        return path
