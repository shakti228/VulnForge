from vulnforge.checks.registry import CheckRegistry

def test_registry():
    registry = CheckRegistry()

    registry.register(
        "test-check",
        lambda metadata: [
            {
                "title": "Test finding",
                "severity": "LOW",
            }
        ],
    )

    result = registry.run({})

    assert registry.names() == ["test-check"]
    assert len(result) == 1
    assert result[0]["title"] == "Test finding"
