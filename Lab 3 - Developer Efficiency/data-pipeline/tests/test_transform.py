"""
Tests for pipeline/transform.py

Covers the core transformation functions.
Checkpoint 4 participants: run these tests to verify your bug fix in normalize_amounts.
Checkpoint 5 participants: add a test for your new transformation function here.
"""

import pytest
import pandas as pd
import numpy as np
from pipeline.transform import (
    drop_duplicates,
    fill_missing_categories,
    normalize_amounts,
    add_high_value_flag,
    run_transformations,
)


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "transaction_id": ["T001", "T002", "T003", "T002"],  # T002 is a duplicate
        "account_id": ["A1", "A2", "A3", "A2"],
        "amount": [100.0, 500.0, 10000.0, 500.0],
        "timestamp": ["2024-01-01T10:00:00", "2024-01-02T11:00:00",
                       "2024-01-03T12:00:00", "2024-01-02T11:00:00"],
        "merchant_category": ["RETAIL", None, "FINANCE", None],
        "late_payment_count": [0, 1, 0, 1],
    })


def test_drop_duplicates_removes_repeated_transaction_ids(sample_df):
    result = drop_duplicates(sample_df)
    assert len(result) == 3
    assert result["transaction_id"].nunique() == 3


def test_fill_missing_categories_replaces_nulls(sample_df):
    result = fill_missing_categories(sample_df)
    assert result["merchant_category"].isnull().sum() == 0
    assert (result["merchant_category"] == "UNKNOWN").sum() == 2


def test_normalize_amounts_produces_zero_to_one_range(sample_df):
    df = drop_duplicates(sample_df)
    result = normalize_amounts(df)
    assert result["amount_normalized"].min() >= 0.0
    assert result["amount_normalized"].max() <= 1.0


def test_normalize_amounts_all_identical_values():
    """
    Regression test for the bug in normalize_amounts.
    When all amounts are the same value, min == max, causing division by zero (NaN).
    After the fix, the column should be returned as-is (or filled with 0.0).
    """
    df = pd.DataFrame({
        "transaction_id": ["T001", "T002"],
        "amount": [250.0, 250.0],
    })
    result = normalize_amounts(df)
    assert not result["amount_normalized"].isnull().any(), (
        "normalize_amounts should not produce NaN when all amounts are equal"
    )


def test_add_high_value_flag_marks_correct_rows(sample_df):
    df = drop_duplicates(sample_df)
    result = add_high_value_flag(df, threshold=1000.0)
    assert result.loc[result["amount"] == 10000.0, "is_high_value"].all()
    assert not result.loc[result["amount"] == 100.0, "is_high_value"].any()
