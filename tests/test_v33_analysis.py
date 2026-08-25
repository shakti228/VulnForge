from vulnforge.analysis.engine import analyze_metadata
from vulnforge.analysis.risk import calculate_risk, risk_level
from vulnforge.analysis.redirects import analyze_redirects
from vulnforge.analysis.response import analyze_response
from vulnforge.analysis.tls import analyze_tls


def test_risk_calculation():
    findings = [
        {"severity": "HIGH"},
        {"severity": "LOW"},
    ]

    assert calculate_risk(findings) == 9
    assert risk_level(9) == "HIGH"


def test_redirect_analysis():
    result = analyze_redirects({
        "url": "https://example.com",
        "redirect_chain": ["a", "b", "c", "d", "e", "f"],
    })

    assert len(result) == 1
    assert result[0]["severity"] == "LOW"


def test_tls_analysis():
    result = analyze_tls({
        "url": "http://example.com",
    })

    assert len(result) == 1
    assert result[0]["severity"] == "MEDIUM"


def test_response_analysis():
    result = analyze_response({
        "url": "https://example.com",
        "headers": {
            "server": "example-server",
            "x-powered-by": "Example",
        },
    })

    assert len(result) == 2


def test_analysis_engine():
    result = analyze_metadata({
        "url": "https://example.com",
        "headers": {},
        "redirect_chain": [],
    })

    assert "findings" in result
    assert "risk_score" in result
    assert "risk_level" in result
