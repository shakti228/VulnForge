from vulnforge.config.targets import load_config
from vulnforge.core.pipeline import VulnForgePipeline

def run_configured_target(target, config_path="vulnforge.json"):
    config = load_config(config_path)
    if config["profile"] != "passive":
        raise ValueError("Only the passive profile is currently supported.")
    return VulnForgePipeline(config["allowed_hosts"]).run(target)
