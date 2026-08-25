import json
from pathlib import Path

def write_security_report(findings, output="reports/security-analysis.json"):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    report = {
        "tool": "VulnForge",
        "version": "1.1.0",
        "mode": "local-passive",
        "finding_count": len(findings),
        "findings": findings,
    }

    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return path
