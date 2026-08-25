from vulnforge.checks.defaults import build_default_registry

def test_default_registry():
    registry = build_default_registry()

    assert "security-headers" in registry.names()

    result = registry.run({
        "url": "https://example.com",
        "status": 200,
        "headers": {},
    })

    assert len(result) == 2
