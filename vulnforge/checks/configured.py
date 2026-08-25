from vulnforge.checks.defaults import build_default_registry

def build_configured_registry(enabled=None):
    registry = build_default_registry()

    if enabled is None:
        return registry

    enabled = {str(name).strip() for name in enabled}

    selected = build_default_registry()
    selected._checks = [
        item for item in selected._checks
        if item[0] in enabled
    ]

    return selected
