"""
Tests for pipeline/ingest.py

Covers load_transactions behaviour: missing files, missing columns, and empty files.
Checkpoint 1 participants: these tests demonstrate what the ingest stage is responsible for.
"""

import pytest
import pandas as pd
from unittest.mock import patch
from io import StringIO
from pipeline.ingest import load_transactions


VALID_CSV = """\
transaction_id,account_id,amount,timestamp,merchant_category
T001,A1,100.0,2024-01-01T10:00:00,RETAIL
T002,A2,500.0,2024-01-02T11:00:00,FINANCE
"""

MISSING_COLUMN_CSV = """\
transaction_id,account_id,amount,timestamp
T001,A1,100.0,2024-01-01T10:00:00
"""

EMPTY_CSV = """\
transaction_id,account_id,amount,timestamp,merchant_category
"""


def test_load_transactions_returns_dataframe(tmp_path):
    source = tmp_path / "transactions.csv"
    source.write_text(VALID_CSV)
    df = load_transactions(str(source))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2


def test_load_transactions_raises_on_missing_file():
    with pytest.raises(FileNotFoundError):
        load_transactions("/nonexistent/path/transactions.csv")


def test_load_transactions_raises_on_missing_columns(tmp_path):
    source = tmp_path / "bad.csv"
    source.write_text(MISSING_COLUMN_CSV)
    with pytest.raises(ValueError, match="missing required columns"):
        load_transactions(str(source))


def test_load_transactions_raises_on_empty_file(tmp_path):
    source = tmp_path / "empty.csv"
    source.write_text(EMPTY_CSV)
    with pytest.raises(ValueError, match="no records"):
        load_transactions(str(source))
