from vulnforge.security.passive_scan import passive_scan

def test_passive_scan(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.security.passive_scan.inspect_http_metadata",
        lambda target: {
            "url": target,
            "status": 200,
            "security_headers": {},
        },
    )

    result = passive_scan("https://example.com")
    assert result["target"] == "https://example.com"
    assert result["finding_count"] == 4
