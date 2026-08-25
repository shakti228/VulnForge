from vulnforge.analyzers.local import LocalProjectAnalyzer
from vulnforge.analyzers.checks import local_checks
from vulnforge.reporting.summary import build_report
from vulnforge.reporting.findings import normalize_findings

def test_report():
    analysis = LocalProjectAnalyzer().analyze(".")
    report = build_report(analysis)
    assert report["tool"] == "VulnForge"
    assert report["author"] == "VYZENTRA"
    assert report["file_count"] >= 1

def test_findings_normalization():
    data = normalize_findings([
        {
            "title": "Test",
            "severity": "INFO",
            "description": "Local test",
            "confidence": "HIGH",
        }
    ])
    assert len(data) == 1
    assert data[0]["title"] == "Test"

def test_local_checks():
    result = local_checks(".")
    assert isinstance(result, list)
