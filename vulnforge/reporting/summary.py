from collections import Counter
from vulnforge.risk.scoring import calculate_risk

def build_summary(findings):
    if isinstance(findings, dict):
        findings = findings.get("findings", [])
    if not isinstance(findings, (list, tuple)):
        findings = []
    valid = [f for f in findings if isinstance(f, dict)]
    counts = Counter(str(f.get("severity", "INFO")).upper() for f in valid)
    return {
        "total": len(valid),
        "critical": counts.get("CRITICAL", 0),
        "high": counts.get("HIGH", 0),
        "medium": counts.get("MEDIUM", 0),
        "low": counts.get("LOW", 0),
        "info": counts.get("INFO", 0),
    }

def build_report(analysis):
    if isinstance(analysis, dict):
        report = dict(analysis)
        report.setdefault("tool", "VulnForge")
        report.setdefault("author", "VYZENTRA")
        report.setdefault("file_count", int(analysis.get("files", 0)))
        findings = analysis.get("findings", [])
    else:
        findings = analysis if isinstance(analysis, list) else []
        report = {"tool": "VulnForge", "author": "VYZENTRA", "file_count": len(findings), "findings": findings}
    report["findings"] = findings if isinstance(findings, list) else []
    report["summary"] = build_summary(report["findings"])
    report["risk_score"] = calculate_risk(report["findings"])
    return report
