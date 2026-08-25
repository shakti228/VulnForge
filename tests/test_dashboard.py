from pathlib import Path
from vulnforge.dashboard.dashboard import build_dashboard

def test_dashboard(tmp_path):
    output = tmp_path / "dashboard.html"
    result = build_dashboard(
        {
            "project": "Test",
            "version": "0.8.0",
            "file_count": 1,
            "findings": [],
        },
        output,
    )
    assert Path(result).exists()
    assert "VulnForge" in Path(result).read_text()
