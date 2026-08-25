from pathlib import Path

class LocalProjectAnalyzer:
    name = "Local Project Analyzer"
    version = "0.2.0"

    def analyze(self, project_path="."):
        root = Path(project_path).resolve()
        excluded = {".git", ".venv", "__pycache__", ".pytest_cache"}
        files = [p for p in root.rglob("*") if p.is_file() and not any(x in excluded for x in p.parts)]
        extensions = {}
        for f in files:
            ext = f.suffix or "[no extension]"
            extensions[ext] = extensions.get(ext, 0) + 1
        return {
            "project": root.name,
            "path": str(root),
            "files": len(files),
            "extensions": extensions,
        }
