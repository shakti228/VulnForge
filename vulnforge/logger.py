import logging
import sys


def setup_logger(level=logging.INFO):
    """Configure the VulnForge application logger."""

    logger = logging.getLogger("vulnforge")
    logger.setLevel(level)

    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "[%(levelname)s] %(name)s: %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
