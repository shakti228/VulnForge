from vulnforge.scanner.authorized import require_authorized
from vulnforge.scanner.http import collect_http_metadata
from vulnforge.checks.defaults import build_default_registry
from vulnforge.risk.scoring import calculate_risk

class ScannerPipeline:
    def __init__(self, allowed_hosts, registry=None):
        self.allowed_hosts = allowed_hosts or []
        self.registry = registry or build_default_registry()

    def run(self, target_url):
        target = require_authorized(target_url, self.allowed_hosts)
        metadata = collect_http_metadata(target)
        findings = self.registry.run(metadata)

        return {
            "target": target.url,
            "metadata": metadata,
            "findings": findings,
            "finding_count": len(findings),
            "risk_score": calculate_risk(findings),
        }
