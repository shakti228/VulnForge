import json
import pytest
from vulnforge.config.profile import run_configured_target

def test_profile_requires_allowlist(tmp_path):
    path = tmp_path / "vulnforge.json"
    path.write_text(json.dumps({
        "allowed_hosts": [],
        "profile": "passive",
    }))

    with pytest.raises(PermissionError):
        run_configured_target("https://example.com", path)
