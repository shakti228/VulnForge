def normalize_findings(findings):
    result = []
    for finding in findings:
        result.append({
            "title": finding.get("title", "Untitled"),
            "severity": finding.get("severity", "INFO"),
            "description": finding.get("description", ""),
            "remediation": finding.get("remediation", ""),
            "confidence": finding.get("confidence", "MEDIUM"),
        })
    return result
