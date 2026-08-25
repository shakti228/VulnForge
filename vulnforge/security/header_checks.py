def check_security_headers(metadata):
    findings = []
    headers = metadata.get("security_headers", {})

    checks = [
        ("strict-transport-security", "HIGH",
         "Strict-Transport-Security header is missing."),
        ("content-security-policy", "MEDIUM",
         "Content-Security-Policy header is missing."),
        ("x-content-type-options", "LOW",
         "X-Content-Type-Options header is missing."),
        ("x-frame-options", "LOW",
         "X-Frame-Options header is missing."),
    ]

    for name, severity, description in checks:
        if not headers.get(name, False):
            findings.append({
                "title": f"Missing security header: {name}",
                "severity": severity,
                "description": description,
                "remediation": f"Review whether {name} should be enabled.",
                "confidence": "MEDIUM",
            })

    return findings
