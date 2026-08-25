from urllib.parse import urlparse

class Target:
    def __init__(self, url):
        self.url = url.rstrip("/")
        parsed = urlparse(self.url)
        self.scheme = parsed.scheme.lower()
        self.host = parsed.hostname or ""

    def validate(self):
        if self.scheme not in {"http", "https"}:
            raise ValueError("Target must use HTTP or HTTPS.")
        if not self.host:
            raise ValueError("Target URL must contain a hostname.")
        return True

    def __repr__(self):
        return f"Target(url={self.url!r}, host={self.host!r})"
