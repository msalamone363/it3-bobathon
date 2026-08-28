"""Logging configuration for the pipeline."""

import logging
import os
from config.settings import LOG_LEVEL, LOG_FILE


def setup_logging():
    """Configure root logger for the pipeline."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(),
        ],
    )
