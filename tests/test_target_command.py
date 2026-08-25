import pytest
from vulnforge.target.command import run_authorized_target

def test_target_command_requires_authorization():
    with pytest.raises(PermissionError):
        run_authorized_target("https://example.com", [])

def test_target_command(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.target.command.VulnForgePipeline.run",
        lambda self, target: {
            "target": target,
            "finding_count": 0,
            "risk_score": 0,
        },
    )

    result = run_authorized_target(
        "https://example.com",
        ["example.com"],
    )

    assert result["target"] == "https://example.com"
    assert result["risk_score"] == 0
