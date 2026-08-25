import pytest
from vulnforge.scanner.target import Target

def test_valid_target():
    target = Target("https://example.com/")
    assert target.validate() is True
    assert target.host == "example.com"

def test_invalid_scheme():
    with pytest.raises(ValueError):
        Target("ftp://example.com").validate()

def test_missing_host():
    with pytest.raises(ValueError):
        Target("https://").validate()
