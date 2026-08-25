from vulnforge.core.pipeline import VulnForgePipeline

def run_authorized_target(target, allowed_hosts):
    return VulnForgePipeline(allowed_hosts).run(target)
