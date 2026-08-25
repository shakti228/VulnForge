import pytest
from vulnforge.core.pipeline import VulnForgePipeline

def test_pipeline_requires_allowlist():
    with pytest.raises(PermissionError):
        VulnForgePipeline().run("https://example.com")

def test_pipeline(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.core.pipeline.run_passive_scan",
        lambda target, allowed_hosts: {
            "target": target,
            "finding_count": 0,
            "risk_score": 0,
            "report": "reports/security-report.json",
        },
    )

    result = VulnForgePipeline(
        ["example.com"]
    ).run("https://example.com")

    assert result["target"] == "https://example.com"
    assert result["risk_score"] == 0
