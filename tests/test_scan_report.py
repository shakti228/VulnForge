from vulnforge.reporting.summary import build_report

def test_scan_report_compatibility():
    analysis = {
        "target": "https://example.com",
        "finding_count": 1,
        "risk_score": 2,
        "findings": [
            {
                "title": "Missing HSTS header",
                "severity": "LOW",
                "description": "Test finding",
                "confidence": "MEDIUM",
            }
        ],
    }

    report = build_report(analysis)

    assert report["tool"] == "VulnForge"
    assert report["author"] == "VYZENTRA"
    assert report["findings"]
    assert report["summary"]["low"] == 1
    assert report["risk_score"] == 2
