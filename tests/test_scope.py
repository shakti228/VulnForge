import pytest
from vulnforge.target.scope import validate_target

def test_allowed_target():
    result = validate_target(
        "https://example.com",
        ["example.com"],
    )
    assert result["host"] == "example.com"

def test_blocked_target():
    with pytest.raises(PermissionError):
        validate_target(
            "https://not-authorized.example",
            ["example.com"],
        )
