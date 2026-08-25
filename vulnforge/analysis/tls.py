def analyze_tls(metadata):
    if not isinstance(metadata, dict):
        return []

    if not metadata.get("url", "").lower().startswith("https://"):
        return [{
            "title": "Target is not using HTTPS",
            "severity": "MEDIUM",
            "description": "The observed target URL does not use HTTPS.",
            "confidence": "HIGH",
            "url": metadata.get("url", ""),
        }]

    return []
