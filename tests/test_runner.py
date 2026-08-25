from vulnforge.security.runner import run_passive_scan

def test_runner(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "vulnforge.security.runner.passive_scan",
        lambda target: {
            "target": target,
            "findings": [
                {
                    "title": "Test",
                    "severity": "LOW",
                    "description": "Test finding",
                }
            ],
        },
    )

    monkeypatch.setattr(
        "vulnforge.security.runner.write_security_report",
        lambda target, findings, score: tmp_path / "report.json",
    )

    result = run_passive_scan(
        "https://example.com",
        ["example.com"],
    )

    assert result["target"] == "https://example.com"
    assert result["finding_count"] == 1
    assert result["risk_score"] == 2
