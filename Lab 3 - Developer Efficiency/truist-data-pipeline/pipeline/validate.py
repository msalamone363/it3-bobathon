"""
Data quality validation module.

Checks transformed data against business rules before loading.

TODO: Add validation rule for transaction_date not being in the future.
TODO: Add configurable threshold for max allowed null percentage per column.
FIXME: validate_no_negative_amounts currently raises on the first failure
       instead of collecting all failures — change to collect and report all.
"""

import pandas as pd
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

ValidationResult = Tuple[bool, List[str]]


def validate_no_nulls(df: pd.DataFrame, columns: List[str]) -> ValidationResult:
    """Check that specified columns contain no null values."""
    failures = []
    for col in columns:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            failures.append(f"Column '{col}' has {null_count} null values")
    return len(failures) == 0, failures


def validate_no_negative_amounts(df: pd.DataFrame) -> ValidationResult:
    """
    Check that no transaction amounts are negative.

    FIXME: currently raises ValueError on first failure.
           Should collect all offending rows and return them as failures.
    """
    negatives = df[df["amount"] < 0]
    if not negatives.empty:
        # FIXME: should not raise — should return (False, [list of issues])
        raise ValueError(f"Found {len(negatives)} transactions with negative amounts")
    return True, []


def validate_amount_normalized_range(df: pd.DataFrame) -> ValidationResult:
    """Check that normalized amounts fall within [0, 1]."""
    failures = []
    out_of_range = df[
        (df["amount_normalized"] < 0) | (df["amount_normalized"] > 1)
    ]
    if not out_of_range.empty:
        failures.append(
            f"{len(out_of_range)} rows have amount_normalized outside [0, 1]"
        )
    return len(failures) == 0, failures


def run_validation(df: pd.DataFrame) -> bool:
    """
    Run all validation checks. Logs failures and returns True only if all pass.

    Args:
        df: Transformed DataFrame.

    Returns:
        True if all validations pass, False otherwise.
    """
    required_columns = ["transaction_id", "account_id", "amount", "timestamp"]
    checks = [
        validate_no_nulls(df, required_columns),
        validate_amount_normalized_range(df),
    ]

    all_passed = True
    for passed, failures in checks:
        if not passed:
            all_passed = False
            for msg in failures:
                logger.warning(f"Validation failure: {msg}")

    if all_passed:
        logger.info("All validation checks passed.")
    else:
        logger.error("Validation completed with failures — review warnings above.")

    return all_passed
