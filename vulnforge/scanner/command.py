from vulnforge.scanner.pipeline import ScannerPipeline

def run_scan(target_url, allowed_hosts):
    return ScannerPipeline(allowed_hosts).run(target_url)
