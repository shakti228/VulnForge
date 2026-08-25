from vulnforge.scanner.pipeline import ScannerPipeline

def test_pipeline(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.scanner.pipeline.collect_http_metadata",
        lambda target: {
            "url": target.url,
            "status": 200,
            "headers": {},
        },
    )

    result = ScannerPipeline(["example.com"]).run(
        "https://example.com"
    )

    assert result["target"] == "https://example.com"
    assert result["finding_count"] == 2
    assert result["risk_score"] == 4
    assert len(result["findings"]) == 2

def test_pipeline_requires_authorization():
    import pytest

    with pytest.raises(PermissionError):
        ScannerPipeline(["example.org"]).run(
            "https://example.com"
        )
