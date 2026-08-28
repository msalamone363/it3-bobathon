"""
Tests for pipeline/validate.py
"""

import pytest
import pandas as pd
from pipeline.validate import (
    validate_no_nulls,
    validate_amount_normalized_range,
    run_validation,
)


@pytest.fixture
def clean_df():
    return pd.DataFrame({
        "transaction_id": ["T001", "T002"],
        "account_id": ["A1", "A2"],
        "amount": [100.0, 500.0],
        "timestamp": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "amount_normalized": [0.1, 0.9],
    })


def test_validate_no_nulls_passes_on_clean_data(clean_df):
    passed, failures = validate_no_nulls(clean_df, ["transaction_id", "account_id"])
    assert passed
    assert failures == []


def test_validate_no_nulls_fails_on_nulls(clean_df):
    clean_df.loc[0, "account_id"] = None
    passed, failures = validate_no_nulls(clean_df, ["account_id"])
    assert not passed
    assert len(failures) == 1


def test_validate_amount_normalized_range_passes(clean_df):
    passed, failures = validate_amount_normalized_range(clean_df)
    assert passed


def test_validate_amount_normalized_range_fails_on_out_of_bounds(clean_df):
    clean_df.loc[0, "amount_normalized"] = 1.5
    passed, failures = validate_amount_normalized_range(clean_df)
    assert not passed


def test_run_validation_returns_true_on_clean_data(clean_df):
    assert run_validation(clean_df) is True
