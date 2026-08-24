import json
from pathlib import Path

from vulnforge.plugins.base import Finding


class JSONReporter:
    name = "JSON Reporter"

    def write(self, findings: list[Finding], output: str = "reports/findings.json") -> Path:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "tool": "VulnForge",
            "version": "0.1.0",
            "author": "VYZENTRA",
            "finding_count": len(findings),
            "findings": [finding.to_dict() for finding in findings],
        }

        path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8",
        )

        return path
