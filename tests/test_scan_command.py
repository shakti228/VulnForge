from vulnforge.scanner.command import run_scan

def test_scan_command(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.scanner.pipeline.collect_http_metadata",
        lambda target: {
            "url": target.url,
            "status": 200,
            "headers": {
                "strict-transport-security": "max-age=31536000",
                "x-content-type-options": "nosniff",
            },
        },
    )

    result = run_scan(
        "https://example.com",
        ["example.com"],
    )

    assert result["target"] == "https://example.com"
    assert result["finding_count"] == 0
    assert result["risk_score"] == 0
