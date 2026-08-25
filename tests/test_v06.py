from vulnforge.core.finding_manager import add_ids
from vulnforge.reporting.severity import severity_summary

def test_finding_ids_are_stable():
    data = [{"title": "Test", "severity": "INFO", "description": "Local"}]
    first = add_ids(data)
    second = add_ids(data)
    assert first[0]["finding_id"] == second[0]["finding_id"]

def test_severity_summary():
    data = [
        {"severity": "INFO"},
        {"severity": "HIGH"},
        {"severity": "INFO"},
    ]
    result = severity_summary(data)
    assert result["INFO"] == 2
    assert result["HIGH"] == 1
