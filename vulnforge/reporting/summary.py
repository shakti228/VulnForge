from datetime import datetime, timezone

def build_report(analysis):
    return {
        "tool": "VulnForge",
        "version": "0.5.0",
        "author": "VYZENTRA",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": analysis["project"],
        "file_count": analysis["files"],
        "file_types": analysis["extensions"],
        "warnings": analysis.get("warnings", []),
    }
