from vulnforge.target.scope import validate_target
from vulnforge.security.passive_scan import passive_scan
from vulnforge.security.dedup import deduplicate_findings
from vulnforge.security.scoring import score_findings
from vulnforge.reporting.security_report import write_security_report

def run_passive_scan(target, allowed_hosts):
    validate_target(target, allowed_hosts)

    result = passive_scan(target)
    findings = deduplicate_findings(result["findings"])
    score = score_findings(findings)

    report = write_security_report(
        target,
        findings,
        score,
    )

    return {
        "target": target,
        "finding_count": len(findings),
        "risk_score": score,
        "report": str(report),
    }
