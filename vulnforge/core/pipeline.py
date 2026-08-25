from vulnforge.security.runner import run_passive_scan

class VulnForgePipeline:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = set(allowed_hosts or [])

    def run(self, target):
        if not self.allowed_hosts:
            raise PermissionError("No authorized target allowlist configured.")

        return run_passive_scan(
            target,
            sorted(self.allowed_hosts),
        )
