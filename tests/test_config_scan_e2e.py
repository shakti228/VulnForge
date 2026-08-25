import json

from vulnforge.config.scanner import load_scanner_config
from vulnforge.checks.configured import build_configured_registry
from vulnforge.scanner.command import run_scan

def test_configured_scan(monkeypatch, tmp_path):
    config_path = tmp_path / "vulnforge.json"

    config_path.write_text(json.dumps({
        "allowed_hosts": ["example.com"],
        "checks": ["security-headers"],
    }))

    config = load_scanner_config(config_path)
    registry = build_configured_registry(config["checks"])

    monkeypatch.setattr(
        "vulnforge.scanner.pipeline.collect_http_metadata",
        lambda target: {
            "url": target.url,
            "status": 200,
            "headers": {},
        },
    )

    result = run_scan(
        "https://example.com",
        config["allowed_hosts"],
        registry=registry,
    )

    assert result["target"] == "https://example.com"
    assert result["finding_count"] == 2
    assert result["findings"][0]["severity"] == "LOW"
