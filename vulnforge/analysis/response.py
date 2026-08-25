def analyze_response(metadata):
    if not isinstance(metadata, dict):
        return []

    findings = []
    headers = metadata.get("headers") or {}

    normalized = {
        str(k).lower(): str(v)
        for k, v in headers.items()
    }

    server = normalized.get("server")

    if server:
        findings.append({
            "title": "Server header disclosed",
            "severity": "INFO",
            "description": "The HTTP response exposes a Server header.",
            "confidence": "HIGH",
            "url": metadata.get("url", ""),
            "evidence": server,
        })

    powered = normalized.get("x-powered-by")

    if powered:
        findings.append({
            "title": "Technology header disclosed",
            "severity": "LOW",
            "description": "The HTTP response exposes an X-Powered-By header.",
            "confidence": "HIGH",
            "url": metadata.get("url", ""),
            "evidence": powered,
        })

    return findings
