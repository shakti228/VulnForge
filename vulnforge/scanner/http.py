from urllib.request import Request, urlopen

def collect_http_metadata(target, timeout=5):
    request = Request(
        target.url,
        method="HEAD",
        headers={"User-Agent": "VulnForge/3.0"},
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            headers = {
                str(k).lower(): str(v)
                for k, v in response.headers.items()
            }

            return {
                "url": target.url,
                "status": response.status,
                "headers": headers,
                "server": headers.get("server", ""),
                "content_type": headers.get("content-type", ""),
            }
    except Exception as exc:
        return {
            "url": target.url,
            "status": None,
            "headers": {},
            "server": "",
            "content_type": "",
            "error": str(exc),
        }
