from urllib.request import Request, urlopen

def inspect_http_metadata(target, timeout=5):
    request = Request(
        target,
        headers={"User-Agent": "VulnForge/1.2"},
        method="GET",
    )

    with urlopen(request, timeout=timeout) as response:
        headers = {k.lower(): v for k, v in response.headers.items()}

        return {
            "url": target,
            "status": response.status,
            "server": headers.get("server", ""),
            "content_type": headers.get("content-type", ""),
            "security_headers": {
                "strict-transport-security":
                    "strict-transport-security" in headers,
                "content-security-policy":
                    "content-security-policy" in headers,
                "x-content-type-options":
                    "x-content-type-options" in headers,
                "x-frame-options":
                    "x-frame-options" in headers,
            },
        }
