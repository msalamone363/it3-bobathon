"""Database connection helpers."""

from sqlalchemy import create_engine, text
from config.settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
import logging

logger = logging.getLogger(__name__)


def get_connection_string() -> str:
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def test_connection() -> bool:
    """Return True if the database is reachable, False otherwise."""
    try:
        engine = create_engine(get_connection_string())
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database connection successful.")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False
