from vulnforge.security.http_metadata import inspect_http_metadata

class FakeHeaders:
    def items(self):
        return [
            ("Content-Type", "text/html"),
            ("X-Content-Type-Options", "nosniff"),
        ]

class FakeResponse:
    status = 200
    headers = FakeHeaders()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

def test_metadata(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.security.http_metadata.urlopen",
        lambda request, timeout: FakeResponse(),
    )

    result = inspect_http_metadata("https://example.com")
    assert result["status"] == 200
    assert result["security_headers"]["x-content-type-options"] is True
