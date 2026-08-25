from vulnforge.checks.registry import CheckRegistry
from vulnforge.scanner.pipeline import ScannerPipeline

def test_custom_check_injection(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.scanner.pipeline.collect_http_metadata",
        lambda target: {
            "url": target.url,
            "status": 200,
            "headers": {},
        },
    )

    registry = CheckRegistry()

    registry.register(
        "custom-check",
        lambda metadata: [{
            "title": "Custom passive finding",
            "severity": "INFO",
            "description": "Test custom check",
            "confidence": "HIGH",
        }],
    )

    result = ScannerPipeline(
        ["example.com"],
        registry=registry,
    ).run("https://example.com")

    assert result["finding_count"] == 1
    assert result["findings"][0]["title"] == "Custom passive finding"
    assert result["risk_score"] == 0
