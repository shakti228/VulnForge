def inspect_metadata(metadata):
    findings = []

    headers = metadata.get("headers", {})
    url = metadata.get("url", "")

    if not metadata.get("status"):
        return findings

    if "strict-transport-security" not in headers:
        findings.append({
            "title": "Missing HSTS header",
            "severity": "LOW",
            "description": "The target response does not advertise Strict-Transport-Security.",
            "confidence": "MEDIUM",
            "url": url,
        })

    if "x-content-type-options" not in headers:
        findings.append({
            "title": "Missing X-Content-Type-Options header",
            "severity": "LOW",
            "description": "The target response does not advertise X-Content-Type-Options.",
            "confidence": "MEDIUM",
            "url": url,
        })

    return findings
