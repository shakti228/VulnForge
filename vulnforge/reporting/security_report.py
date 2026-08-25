import json
from pathlib import Path

def write_security_report(
    target,
    findings,
    score,
    output="reports/security-report.json",
):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "tool": "VulnForge",
        "version": "1.4.0",
        "mode": "passive-authorized",
        "target": target,
        "finding_count": len(findings),
        "risk_score": score,
        "findings": findings,
    }

    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path
