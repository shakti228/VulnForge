from vulnforge.scanner.target import Target

def is_authorized(target_url, allowed_hosts):
    target = Target(target_url)
    target.validate()

    allowed = {
        str(host).lower().strip()
        for host in (allowed_hosts or [])
        if str(host).strip()
    }

    return target.host.lower() in allowed

def require_authorized(target_url, allowed_hosts):
    if not is_authorized(target_url, allowed_hosts):
        raise PermissionError(
            f"Target is not authorized: {target_url}"
        )
    return Target(target_url)
