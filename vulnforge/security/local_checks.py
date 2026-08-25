from pathlib import Path

EXCLUDED = {".git", ".venv", "__pycache__", ".pytest_cache"}

def scan_local_project(project_path="."):
    root = Path(project_path).resolve()
    findings = []

    for path in root.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED for part in path.parts):
            continue

        rel = str(path.relative_to(root))

        if path.name in {".env", ".env.local", ".env.production"}:
            findings.append({
                "title": "Sensitive configuration file",
                "severity": "INFO",
                "description": f"Sensitive configuration file found: {rel}",
                "remediation": "Keep secrets outside version control.",
                "confidence": "HIGH",
            })

        if path.suffix.lower() in {".pem", ".key"}:
            findings.append({
                "title": "Potential private-key file",
                "severity": "MEDIUM",
                "description": f"Potential key material found: {rel}",
                "remediation": "Verify that private key material is not committed.",
                "confidence": "MEDIUM",
            })

        try:
            if path.stat().st_size > 5 * 1024 * 1024:
                findings.append({
                    "title": "Large file detected",
                    "severity": "INFO",
                    "description": f"File larger than 5 MB: {rel}",
                    "remediation": "Review whether the file belongs in the repository.",
                    "confidence": "HIGH",
                })
        except OSError:
            continue

    return findings
