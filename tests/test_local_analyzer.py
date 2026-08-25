from vulnforge.analyzers.local import LocalProjectAnalyzer
from vulnforge.dashboard.summary import build_summary

def test_local_analyzer():
    result = LocalProjectAnalyzer().analyze(".")
    assert result["project"] == "VulnForge"
    assert result["files"] >= 1
    assert ".git" not in result["extensions"]

def test_summary():
    result = LocalProjectAnalyzer().analyze(".")
    summary = build_summary(result)
    assert summary["project"] == "VulnForge"
    assert summary["files"] >= 1
    assert summary["file_types"] >= 1
