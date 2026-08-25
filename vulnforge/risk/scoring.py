SEVERITY_SCORE = {
    "CRITICAL": 10,
    "HIGH": 7,
    "MEDIUM": 4,
    "LOW": 2,
    "INFO": 0,
}

def calculate_risk(findings):
    if not isinstance(findings, (list, tuple)):
        return 0

    return sum(
        SEVERITY_SCORE.get(
            str(f.get("severity", "INFO")).upper(), 0
        )
        for f in findings
        if isinstance(f, dict)
    )
