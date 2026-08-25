from vulnforge.auditors.config_audit import audit_project

def test_config_audit_returns_list():
    result = audit_project(".")
    assert isinstance(result, list)

def test_config_audit_does_not_scan_git():
    result = audit_project(".")
    for finding in result:
        assert ".git" not in finding["description"]
