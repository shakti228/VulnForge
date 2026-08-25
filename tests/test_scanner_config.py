import json

from vulnforge.config.scanner import load_scanner_config

def test_load_scanner_config(tmp_path):
    path = tmp_path / "vulnforge.json"

    path.write_text(json.dumps({
        "allowed_hosts": ["example.com"],
        "checks": ["security-headers"],
    }))

    result = load_scanner_config(path)

    assert result["allowed_hosts"] == ["example.com"]
    assert result["checks"] == ["security-headers"]

def test_missing_config(tmp_path):
    result = load_scanner_config(tmp_path / "missing.json")

    assert result["allowed_hosts"] == []
    assert result["checks"] is None
