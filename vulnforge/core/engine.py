from dataclasses import dataclass

from vulnforge.plugins.base import Finding, Plugin
from vulnforge.plugins.registry import PluginRegistry


@dataclass
class EngineResult:
    status: str
    message: str
    findings: list[Finding]


class VulnForgeEngine:
    def __init__(self):
        self.registry = PluginRegistry()

    def register_plugin(self, plugin: Plugin) -> None:
        self.registry.register(plugin)

    def run(self) -> EngineResult:
        findings = []

        for plugin in self.registry.get_all():
            try:
                findings.extend(plugin.run())
            except Exception as exc:
                findings.append(Finding(title=f"Plugin Error: {plugin.name}", severity="ERROR", description=str(exc), remediation="Review the plugin implementation.", confidence="HIGH"))

        return EngineResult(
            status="success",
            message=f"Executed {len(self.registry.get_all())} plugin(s)",
            findings=findings,
        )
