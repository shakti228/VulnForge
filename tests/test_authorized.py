import pytest
from vulnforge.scanner.authorized import is_authorized, require_authorized

def test_authorized_host():
    assert is_authorized(
        "https://example.com",
        ["example.com"],
    )

def test_unauthorized_host():
    assert not is_authorized(
        "https://example.com",
        ["example.org"],
    )

def test_require_authorized():
    target = require_authorized(
        "https://example.com",
        ["example.com"],
    )
    assert target.host == "example.com"

def test_require_rejects():
    with pytest.raises(PermissionError):
        require_authorized(
            "https://example.com",
            ["example.org"],
        )
