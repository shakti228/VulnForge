import json
from pathlib import Path

from vulnforge.plugins.base import Finding


class JSONReporter:
    name = "JSON Reporter"

    def write(self, findings: list[Finding], output: str = "reports/findings.json") -> Path:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        summary = {level: sum(1 for f in findings if f.severity.upper() == level) for level in ["INFO","LOW","MEDIUM","HIGH","CRITICAL"]}; summary = {level: sum(1 for f in findings if f.severity.upper() == level) for level in ["INFO","LOW","MEDIUM","HIGH","CRITICAL"]}; data = {
            "tool": "VulnForge",
            "version": "0.1.0",
            "author": "VYZENTRA",
            "finding_count": len(findings),
            "severity_summary": summary,
            "severity_summary": summary,
            "findings": [finding.to_dict() for finding in findings],
        }

        path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8",
        )

        return path
