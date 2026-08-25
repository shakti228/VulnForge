from vulnforge.security.http_metadata import inspect_http_metadata
from vulnforge.security.header_checks import check_security_headers

def passive_scan(target):
    metadata = inspect_http_metadata(target)
    findings = check_security_headers(metadata)

    return {
        "target": target,
        "metadata": metadata,
        "finding_count": len(findings),
        "findings": findings,
    }
