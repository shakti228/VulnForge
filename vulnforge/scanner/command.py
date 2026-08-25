from vulnforge.scanner.pipeline import ScannerPipeline

def run_scan(target_url, allowed_hosts, registry=None):
    return ScannerPipeline(
        allowed_hosts,
        registry=registry,
    ).run(target_url)
