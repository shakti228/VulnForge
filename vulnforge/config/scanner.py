import json
from pathlib import Path

def load_scanner_config(path="vulnforge.json"):
    config_path = Path(path)

    if not config_path.exists():
        return {
            "allowed_hosts": [],
            "checks": None,
        }

    data = json.loads(config_path.read_text(encoding="utf-8"))

    allowed_hosts = data.get("allowed_hosts", [])
    checks = data.get("checks")

    if not isinstance(allowed_hosts, list):
        raise ValueError("allowed_hosts must be a list.")

    if checks is not None and not isinstance(checks, list):
        raise ValueError("checks must be a list.")

    return {
        "allowed_hosts": allowed_hosts,
        "checks": checks,
    }
