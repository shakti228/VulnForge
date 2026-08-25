from vulnforge.security.scoring import score_finding, score_findings

def test_score_finding():
    assert score_finding({"severity": "HIGH"}) == 8

def test_score_findings():
    assert score_findings([
        {"severity": "HIGH"},
        {"severity": "LOW"},
        {"severity": "INFO"},
    ]) == 10
