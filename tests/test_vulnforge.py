from vulnforge.core.engine import VulnForgeEngine
from vulnforge.plugins.test_plugin import TestPlugin


def test_plugin_execution():
    engine = VulnForgeEngine()
    engine.register_plugin(TestPlugin())

    result = engine.run()

    assert result.status == "success"
    assert len(result.findings) == 1
    assert result.findings[0].title == "Plugin System Check"
    assert result.findings[0].severity == "INFO"


def test_finding_metadata():
    engine = VulnForgeEngine()
    engine.register_plugin(TestPlugin())

    result = engine.run()
    finding = result.findings[0]

    assert finding.finding_id
    assert finding.timestamp
    assert finding.confidence == "HIGH"
    assert finding.remediation


def test_local_analyzer():
    from vulnforge.analyzers.local import LocalProjectAnalyzer
    r=LocalProjectAnalyzer().analyze(".")
    assert r["project"] == "VulnForge"
    assert r["files"] >= 1
