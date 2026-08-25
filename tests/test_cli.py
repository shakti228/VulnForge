import subprocess

def test_help():
    result = subprocess.run(
        ["vulnforge", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "VulnForge" in result.stdout

def test_version():
    result = subprocess.run(
        ["vulnforge", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "3.0.0" in result.stdout

def test_analyze():
    result = subprocess.run(
        ["vulnforge", "analyze"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Project: VulnForge" in result.stdout
