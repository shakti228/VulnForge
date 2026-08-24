from vulnforge.plugins.base import Plugin


class PluginRegistry:
    def __init__(self):
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        if plugin.name in self._plugins:
            raise ValueError(f"Plugin already registered: {plugin.name}")
        self._plugins[plugin.name] = plugin

    def get_all(self) -> list[Plugin]:
        return list(self._plugins.values())

    def get(self, name: str) -> Plugin | None:
        return self._plugins.get(name)
