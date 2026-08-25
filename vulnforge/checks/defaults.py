from vulnforge.checks.registry import CheckRegistry
from vulnforge.scanner.findings import inspect_metadata
from vulnforge.checks.web_headers import check_web_headers, check_cookie_flags

def build_default_registry():
    registry = CheckRegistry()
    registry.register("security-headers", inspect_metadata)
    return registry
