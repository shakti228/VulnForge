from vulnforge.checks.configured import build_configured_registry

def test_enabled_checks():
    registry = build_configured_registry(["security-headers"])

    assert registry.names() == ["security-headers"]

def test_disabled_checks():
    registry = build_configured_registry([])

    assert registry.names() == []
