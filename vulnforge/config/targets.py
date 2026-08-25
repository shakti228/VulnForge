from pathlib import Path
import json

DEFAULT_CONFIG = {
    "allowed_hosts": [],
    "profile": "passive",
}

def load_config(path="vulnforge.json"):
    config_path = Path(path)

    if not config_path.exists():
        return dict(DEFAULT_CONFIG)

    data = json.loads(config_path.read_text(encoding="utf-8"))

    return {
        "allowed_hosts": list(data.get("allowed_hosts", [])),
        "profile": data.get("profile", "passive"),
    }
