from vulnforge.checks.registry import CheckRegistry
from vulnforge.scanner.findings import inspect_metadata

def build_default_registry():
    registry = CheckRegistry()
    registry.register("security-headers", inspect_metadata)
    return registry
