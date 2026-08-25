from vulnforge.security.header_checks import check_security_headers

def test_missing_headers():
    result = check_security_headers({"security_headers": {}})
    assert len(result) == 4

def test_all_headers_present():
    result = check_security_headers({
        "security_headers": {
            "strict-transport-security": True,
            "content-security-policy": True,
            "x-content-type-options": True,
            "x-frame-options": True,
        }
    })
    assert result == []
