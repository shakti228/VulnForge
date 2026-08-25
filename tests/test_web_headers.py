from vulnforge.checks.web_headers import check_web_headers, check_cookie_flags

def test_web_header_checks():
    result = check_web_headers({
        "url": "https://example.com",
        "headers": {},
    })

    titles = {item["title"] for item in result}

    assert "Missing Content-Security-Policy" in titles
    assert "Missing Referrer-Policy" in titles
    assert "Missing Permissions-Policy" in titles

def test_cookie_flags():
    result = check_cookie_flags({
        "url": "https://example.com",
        "headers": {
            "set-cookie": "session=test",
        },
    })

    titles = {item["title"] for item in result}

    assert "Cookie without Secure attribute" in titles
    assert "Cookie without HttpOnly attribute" in titles

def test_no_cookie():
    assert check_cookie_flags({"headers": {}}) == []
