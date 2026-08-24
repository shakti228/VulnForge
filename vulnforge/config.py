from dataclasses import dataclass


@dataclass
class VulnForgeConfig:
    app_name: str = "VulnForge"
    version: str = "0.1.0"
    author: str = "VYZENTRA"
    log_level: str = "INFO"


def get_config() -> VulnForgeConfig:
    return VulnForgeConfig()
