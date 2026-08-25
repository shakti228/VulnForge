from vulnforge.analysis.redirects import analyze_redirects
from vulnforge.analysis.response import analyze_response
from vulnforge.analysis.risk import calculate_risk, risk_level
from vulnforge.analysis.tls import analyze_tls


def analyze_metadata(metadata, existing_findings=None):
    findings = []

    if isinstance(existing_findings, (list, tuple)):
        findings.extend(
            item for item in existing_findings
            if isinstance(item, dict)
        )

    findings.extend(analyze_redirects(metadata))
    findings.extend(analyze_tls(metadata))
    findings.extend(analyze_response(metadata))

    score = calculate_risk(findings)

    return {
        "findings": findings,
        "risk_score": score,
        "risk_level": risk_level(score),
    }
