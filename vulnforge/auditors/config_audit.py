from pathlib import Path

IGNORED = {".git", ".venv", "__pycache__", ".pytest_cache"}

def audit_project(project_path="."):
    root = Path(project_path).resolve()
    findings = []

    for path in root.rglob("*"):
        if not path.is_file() or any(x in IGNORED for x in path.parts):
            continue

        if path.name in {".env", ".env.local", ".env.production"}:
            findings.append({
                "title": "Sensitive configuration file present",
                "severity": "INFO",
                "description": f"Configuration file found: {path.relative_to(root)}",
                "remediation": "Keep secrets outside source control and use appropriate secret management.",
                "confidence": "HIGH",
            })

    return findings
