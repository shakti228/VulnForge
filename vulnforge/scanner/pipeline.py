from vulnforge.scanner.authorized import require_authorized
from vulnforge.scanner.http import collect_http_metadata
from vulnforge.scanner.findings import inspect_metadata
from vulnforge.risk.scoring import calculate_risk

class ScannerPipeline:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts or []

    def run(self, target_url):
        target = require_authorized(target_url, self.allowed_hosts)
        metadata = collect_http_metadata(target)
        findings = inspect_metadata(metadata)

        return {
            "target": target.url,
            "metadata": metadata,
            "findings": findings,
            "finding_count": len(findings),
            "risk_score": calculate_risk(findings),
        }
