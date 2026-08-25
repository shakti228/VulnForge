import importlib
import pkgutil
from vulnforge.plugins.base import Plugin

class PluginRegistry:
    def __init__(self): self._plugins={}
    def register(self, plugin):
        if plugin.name in self._plugins: raise ValueError(f"Plugin already registered: {plugin.name}")
        self._plugins[plugin.name]=plugin
    def get_all(self): return list(self._plugins.values())
    def get(self,name): return self._plugins.get(name)
    def discover(self):
        package=importlib.import_module("vulnforge.plugins")
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            if module_name.startswith("_") or module_name in {"base","registry"}: continue
            module=importlib.import_module(f"vulnforge.plugins.{module_name}")
            for obj in module.__dict__.values():
                if isinstance(obj,type) and issubclass(obj,Plugin) and obj is not Plugin: self.register(obj())
