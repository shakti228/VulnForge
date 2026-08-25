SEVERITY_SCORE = {
    "CRITICAL": 10,
    "HIGH": 8,
    "MEDIUM": 5,
    "LOW": 2,
    "INFO": 0,
}

def score_finding(finding):
    severity = str(finding.get("severity", "INFO")).upper()
    return SEVERITY_SCORE.get(severity, 0)

def score_findings(findings):
    return sum(score_finding(f) for f in findings)
