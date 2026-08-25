def check_web_headers(metadata):
    headers = {
        str(k).lower(): str(v)
        for k, v in (metadata.get("headers") or {}).items()
    }
    url = metadata.get("url", "")
    findings = []

    checks = [
        (
            "Missing Content-Security-Policy",
            "MEDIUM",
            "The response does not advertise a Content-Security-Policy header.",
        ),
        (
            "Missing Referrer-Policy",
            "LOW",
            "The response does not advertise a Referrer-Policy header.",
        ),
        (
            "Missing Permissions-Policy",
            "LOW",
            "The response does not advertise a Permissions-Policy header.",
        ),
    ]

    for title, severity, description in checks:
        header = {
            "Missing Content-Security-Policy": "content-security-policy",
            "Missing Referrer-Policy": "referrer-policy",
            "Missing Permissions-Policy": "permissions-policy",
        }[title]

        if header not in headers:
            findings.append({
                "title": title,
                "severity": severity,
                "description": description,
                "confidence": "MEDIUM",
                "url": url,
            })

    return findings


def check_cookie_flags(metadata):
    headers = {
        str(k).lower(): str(v)
        for k, v in (metadata.get("headers") or {}).items()
    }

    set_cookie = headers.get("set-cookie", "")
    if not set_cookie:
        return []

    findings = []

    if "secure" not in set_cookie.lower():
        findings.append({
            "title": "Cookie without Secure attribute",
            "severity": "LOW",
            "description": "A Set-Cookie response was observed without a Secure attribute.",
            "confidence": "MEDIUM",
            "url": metadata.get("url", ""),
        })

    if "httponly" not in set_cookie.lower():
        findings.append({
            "title": "Cookie without HttpOnly attribute",
            "severity": "LOW",
            "description": "A Set-Cookie response was observed without an HttpOnly attribute.",
            "confidence": "MEDIUM",
            "url": metadata.get("url", ""),
        })

    return findings
