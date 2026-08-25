def build_summary(analysis):
    return {
        "project": analysis["project"],
        "files": analysis["files"],
        "file_types": len(analysis["extensions"]),
        "extensions": analysis["extensions"],
        "warnings": analysis.get("warnings", []),
    }
