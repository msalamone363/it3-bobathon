"""
Data ingestion module.

Reads raw transaction data from CSV source files and returns a
cleaned DataFrame ready for the transformation stage.

TODO: Add support for reading from S3 in addition to local filesystem.
TODO: Add schema validation on ingest (column names, dtypes).
"""

import pandas as pd
import logging
from config.settings import SOURCE_FILE_PATH, BATCH_SIZE

logger = logging.getLogger(__name__)


def load_transactions(file_path: str = SOURCE_FILE_PATH) -> pd.DataFrame:
    """
    Load raw transaction records from a CSV file.

    Args:
        file_path: Path to the CSV file containing raw transactions.

    Returns:
        DataFrame with raw transaction data.

    Raises:
        FileNotFoundError: If the source file does not exist.
        ValueError: If the file is empty or missing required columns.
    """
    logger.info(f"Loading transactions from {file_path}")

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        logger.error(f"Source file not found: {file_path}")
        raise

    required_columns = [
        "transaction_id",
        "account_id",
        "amount",
        "timestamp",
        "merchant_category",
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Source file missing required columns: {missing}")

    if df.empty:
        raise ValueError("Source file contains no records.")

    logger.info(f"Loaded {len(df)} transactions")
    return df


def load_transactions_in_batches(file_path: str = SOURCE_FILE_PATH):
    """
    Generator that yields transaction data in chunks of BATCH_SIZE rows.
    Use this for large files that don't fit in memory.

    Args:
        file_path: Path to the CSV file.

    Yields:
        DataFrame chunks of up to BATCH_SIZE rows.
    """
    for chunk in pd.read_csv(file_path, chunksize=BATCH_SIZE):
        yield chunk
