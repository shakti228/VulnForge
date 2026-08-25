from urllib.parse import urlparse

def validate_target(url, allowed_hosts):
    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Only HTTP/HTTPS targets are supported.")

    host = parsed.hostname
    if not host:
        raise ValueError("Target hostname is missing.")

    if host not in set(allowed_hosts):
        raise PermissionError(
            f"Target '{host}' is not in the authorized allowlist."
        )

    return {
        "url": url,
        "host": host,
        "scheme": parsed.scheme,
    }
