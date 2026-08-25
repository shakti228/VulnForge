from vulnforge.config.profile import run_configured_target

def scan(target, config_path="vulnforge.json"):
    return run_configured_target(target, config_path)
