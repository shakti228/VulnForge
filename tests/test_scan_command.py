from vulnforge.commands.scan import scan

def test_scan_command(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.commands.scan.run_configured_target",
        lambda target, config_path="vulnforge.json": {
            "target": target,
            "finding_count": 0,
            "risk_score": 0,
        },
    )

    result = scan("https://example.com")
    assert result["target"] == "https://example.com"
    assert result["risk_score"] == 0
