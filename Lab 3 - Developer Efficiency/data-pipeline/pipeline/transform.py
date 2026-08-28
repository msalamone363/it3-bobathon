"""
Data transformation module.

Cleans and enriches raw transaction data before loading.
Contains a pre-planted bug for Checkpoint 4 — see the normalize_amounts function.
"""

import pandas as pd
import numpy as np
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate transactions based on transaction_id."""
    before = len(df)
    df = df.drop_duplicates(subset=["transaction_id"])
    removed = before - len(df)
    if removed:
        logger.info(f"Removed {removed} duplicate transactions")
    return df


def fill_missing_categories(df: pd.DataFrame, default: str = "UNKNOWN") -> pd.DataFrame:
    """Fill null merchant_category values with a default placeholder."""
    df["merchant_category"] = df["merchant_category"].fillna(default)
    return df


def parse_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the timestamp column from string to datetime.

    TODO: Handle multiple timestamp formats — currently assumes ISO 8601 only.
    """
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["transaction_date"] = df["timestamp"].dt.date
    df["transaction_hour"] = df["timestamp"].dt.hour
    return df


def normalize_amounts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize transaction amounts to a 0–1 range using min-max scaling.

    BUG: This function divides by (max - min) but does not handle the case
    where all amounts are identical (division by zero produces NaN silently).
    Fix: add a guard clause to return the original column unchanged when
    max == min.
    """
    min_val = df["amount"].min()
    max_val = df["amount"].max()

    # BUG IS HERE: no guard for max_val == min_val
    df["amount_normalized"] = (df["amount"] - min_val) / (max_val - min_val)
    return df


def add_high_value_flag(df: pd.DataFrame, threshold: float = 10000.0) -> pd.DataFrame:
    """Flag transactions above a dollar threshold as high-value."""
    df["is_high_value"] = df["amount"] > threshold
    return df


def run_transformations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run the full transformation pipeline in order.

    Args:
        df: Raw transaction DataFrame from the ingest stage.

    Returns:
        Transformed DataFrame ready for validation and loading.
    """
    df = drop_duplicates(df)
    df = fill_missing_categories(df)
    df = parse_timestamps(df)
    df = normalize_amounts(df)
    df = add_high_value_flag(df)
    logger.info(f"Transformation complete. {len(df)} records processed.")
    return df
