def severity_summary(findings):
    summary = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
    for finding in findings:
        severity = str(finding.get("severity", "INFO")).upper()
        summary[severity] = summary.get(severity, 0) + 1
    return summary
