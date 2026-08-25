from vulnforge.risk.scoring import calculate_risk

def test_risk_score():
    findings = [
        {"severity": "CRITICAL"},
        {"severity": "HIGH"},
        {"severity": "MEDIUM"},
        {"severity": "LOW"},
        {"severity": "INFO"},
    ]

    assert calculate_risk(findings) == 23

def test_empty_risk():
    assert calculate_risk([]) == 0
