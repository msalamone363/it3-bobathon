"""
Data loader module.

Writes validated, transformed data to the destination data warehouse.

TODO: Add support for upsert (update existing rows) in addition to append.
TODO: Add row-count reconciliation check after load.
"""

import pandas as pd
import logging
from sqlalchemy import create_engine
from config.settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

logger = logging.getLogger(__name__)


def get_engine():
    """Create and return a SQLAlchemy database engine."""
    connection_string = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(connection_string)


def load_to_warehouse(
    df: pd.DataFrame,
    table_name: str = "fact_transactions",
    if_exists: str = "append",
) -> int:
    """
    Load a DataFrame into the data warehouse.

    Args:
        df: Validated, transformed DataFrame.
        table_name: Target table in the data warehouse.
        if_exists: Behavior when table exists — 'append', 'replace', or 'fail'.

    Returns:
        Number of rows written.
    """
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    logger.info(f"Loaded {len(df)} rows into {table_name}")
    return len(df)
