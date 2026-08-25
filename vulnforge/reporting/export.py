import json
from pathlib import Path

def export_json(data, output="reports/vulnforge-report.json"):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return str(path)
