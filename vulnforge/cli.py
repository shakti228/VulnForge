import argparse

from vulnforge.config import get_config
from vulnforge.core.engine import VulnForgeEngine
from vulnforge.logger import setup_logger
from vulnforge.reporters.json_reporter import JSONReporter
from vulnforge.reporters.html_reporter import HTMLReporter


def main():
    config = get_config()
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        prog="vulnforge",
        description=f"{config.app_name} - Security Research & Analysis Platform",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{config.app_name} {config.version}",
    )

    parser.add_argument("command", nargs="?", choices=["scan","analyze"], help="Run an authorized security analysis")

    parser.add_argument(
        "--about",
        action="store_true",
        help="Show project information",
    )

    args = parser.parse_args()

    if args.command == "analyze":
        from vulnforge.analyzers.local import LocalProjectAnalyzer
        result=LocalProjectAnalyzer().analyze("."); logger.info("Local project: %s | Files: %s", result["project"], result["files"]); logger.info("File types: %s", result["extensions"]); return

    if args.command == "scan":
        engine = VulnForgeEngine(); engine.registry.discover(); result = engine.run(); logger.info(result.message); [logger.info("[%s] %s — %s", f.severity, f.title, f.description) for f in result.findings]; JSONReporter().write(result.findings); HTMLReporter().write(result.findings); logger.info("Reports generated successfully"); return

    if args.about:
        print()
        print(config.app_name)
        print("Security Research & Analysis Platform")
        print(f"Version: {config.version}")
        print(f"Made by {config.author}")
        print()
        return

    engine = VulnForgeEngine()
    engine.register_plugin(TestPlugin())

    logger.info("%s initialized", config.app_name)

    result = engine.run()
    logger.info(result.message)

    for finding in result.findings:
        logger.info(
            "[%s] %s — %s",
            finding.severity,
            finding.title,
            finding.description,
        )

    report = JSONReporter()
    path = report.write(result.findings)

    logger.info("JSON report written to %s", path)

    html_report = HTMLReporter()
    html_path = html_report.write(result.findings)
    logger.info("HTML report written to %s", html_path)


if __name__ == "__main__":
    main()
