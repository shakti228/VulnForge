import argparse
import json
from pathlib import Path

from vulnforge.analyzers.local import LocalProjectAnalyzer
from vulnforge.dashboard.dashboard import build_dashboard
from vulnforge.reporting.export import export_json

VERSION = "0.9.0"

def main():
    parser = argparse.ArgumentParser(
        prog="vulnforge",
        description="VulnForge - Security Research & Analysis Platform",
    )
    parser.add_argument("--version", action="version", version=f"VulnForge {VERSION}")
    parser.add_argument("--about", action="store_true")

    sub = parser.add_subparsers(dest="command")
    sub.add_parser("analyze", help="Analyze the local project")
    sub.add_parser("report", help="Generate a local JSON and HTML report")

    args = parser.parse_args()

    if args.about:
        print("VulnForge")
        print("Security Research & Analysis Platform")
        print(f"Version: {VERSION}")
        print("Made by VYZENTRA")
        return

    if args.command == "analyze":
        result = LocalProjectAnalyzer().analyze(".")
        print(f"Project: {result['project']}")
        print(f"Files: {result['files']}")
        print(f"File types: {result['extensions']}")
        return

    if args.command == "report":
        analysis = LocalProjectAnalyzer().analyze(".")
        report = {
            "tool": "VulnForge",
            "version": VERSION,
            "author": "VYZENTRA",
            "project": analysis["project"],
            "file_count": analysis["files"],
            "file_types": analysis["extensions"],
            "warnings": analysis.get("warnings", []),
            "findings": [],
        }

        json_path = export_json(report)
        html_path = build_dashboard(report)

        print(f"JSON report: {json_path}")
        print(f"HTML report: {html_path}")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
