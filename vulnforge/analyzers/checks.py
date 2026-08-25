from pathlib import Path

SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
}

def local_checks(project_path="."):
    root = Path(project_path).resolve()
    excluded = {".git", ".venv", "__pycache__", ".pytest_cache"}
    findings = []

    for p in root.rglob("*"):
        if not p.is_file() or any(x in excluded for x in p.parts):
            continue
        if p.name in SENSITIVE_NAMES:
            findings.append({
                "title": "Sensitive configuration file detected",
                "severity": "INFO",
                "description": f"Local file found: {p.relative_to(root)}",
                "remediation": "Ensure sensitive configuration is not committed to version control.",
                "confidence": "HIGH",
            })

    return findings
