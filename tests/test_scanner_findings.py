from vulnforge.scanner.findings import inspect_metadata

def test_security_header_findings():
    result = inspect_metadata({
        "url": "https://example.com",
        "status": 200,
        "headers": {},
    })

    titles = {item["title"] for item in result}

    assert "Missing HSTS header" in titles
    assert "Missing X-Content-Type-Options header" in titles

def test_secure_headers():
    result = inspect_metadata({
        "url": "https://example.com",
        "status": 200,
        "headers": {
            "strict-transport-security": "max-age=31536000",
            "x-content-type-options": "nosniff",
        },
    })

    assert result == []
