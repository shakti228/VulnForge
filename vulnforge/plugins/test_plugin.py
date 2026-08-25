from vulnforge.plugins.base import Finding, Plugin

class TestPlugin(Plugin):
    name = "Local Test Plugin"
    version = "0.2.0"
    def run(self) -> list[Finding]:
        return [Finding(title="Plugin System Check", severity="INFO", description="Local plugin executed successfully.", remediation="No action required. This is a local architecture test.", confidence="HIGH")]
