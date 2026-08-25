from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    app_name: str = "VulnForge"
    version: str = "0.3.0"
    author: str = "VYZENTRA"
    report_dir: str = "reports"

def get_config() -> Config:
    return Config()
