import json
from pathlib import Path

def write_target_report(data, output="reports/target-metadata.json"):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path
