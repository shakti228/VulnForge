def analyze_redirects(metadata):
    if not isinstance(metadata, dict):
        return []

    chain = metadata.get("redirect_chain", [])

    if not isinstance(chain, (list, tuple)):
        return []

    findings = []

    if len(chain) > 5:
        findings.append({
            "title": "Long redirect chain",
            "severity": "LOW",
            "description": "The observed response used more than five redirects.",
            "confidence": "HIGH",
            "url": metadata.get("url", ""),
        })

    return findings
