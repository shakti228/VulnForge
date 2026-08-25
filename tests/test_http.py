from vulnforge.scanner.http import collect_http_metadata

class FakeResponse:
    status = 200
    headers = {
        "Server": "TestServer",
        "Content-Type": "text/html",
    }

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

def test_http_metadata(monkeypatch):
    monkeypatch.setattr(
        "vulnforge.scanner.http.urlopen",
        lambda request, timeout=5: FakeResponse(),
    )

    class Target:
        url = "https://example.com"

    result = collect_http_metadata(Target())

    assert result["status"] == 200
    assert result["server"] == "TestServer"
    assert result["content_type"] == "text/html"
