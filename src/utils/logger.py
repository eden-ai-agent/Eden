"""Utility for obtaining a configured logger."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a simple console logger with ``INFO`` level."""

    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

