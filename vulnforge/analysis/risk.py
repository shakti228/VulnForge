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

    score = sum(
        SEVERITY_SCORE.get(
            str(item.get("severity", "INFO")).upper(), 0
        )
        for item in findings
        if isinstance(item, dict)
    )

    return min(score, 100)


def risk_level(score):
    if score >= 10:
        return "CRITICAL"
    if score >= 7:
        return "HIGH"
    if score >= 4:
        return "MEDIUM"
    if score >= 1:
        return "LOW"
    return "INFO"
