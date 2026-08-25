from vulnforge.reporting.summary import build_summary

def test_summary():
    result = build_summary([
        {"severity": "HIGH"},
        {"severity": "HIGH"},
        {"severity": "MEDIUM"},
        {"severity": "LOW"},
        {"severity": "INFO"},
    ])

    assert result == {
        "total": 5,
        "critical": 0,
        "high": 2,
        "medium": 1,
        "low": 1,
        "info": 1,
    }

def test_empty_summary():
    result = build_summary([])
    assert result["total"] == 0
