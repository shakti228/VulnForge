from vulnforge.security.local_checks import scan_local_project

def test_local_security_scan_returns_list():
    result = scan_local_project(".")
    assert isinstance(result, list)

def test_local_security_does_not_use_external_targets():
    result = scan_local_project(".")
    assert all("http://" not in str(x) and "https://" not in str(x) for x in result)
