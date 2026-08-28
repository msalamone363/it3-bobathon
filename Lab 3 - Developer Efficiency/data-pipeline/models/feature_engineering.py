"""
Feature engineering for the credit risk scoring model.

Extracts and scales features from raw account and transaction data
before passing them to the risk scorer.

TODO: Add feature for rolling 30-day transaction velocity.
TODO: Cache feature matrix to avoid recomputing on repeated calls.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from config.settings import FEATURE_COLUMNS
import logging

logger = logging.getLogger(__name__)


def compute_account_features(transactions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate per-account features from transaction history.

    Args:
        transactions_df: Raw or transformed transaction DataFrame with
                         at minimum: account_id, amount, timestamp, late_payment_count.

    Returns:
        DataFrame indexed by account_id with one row per account containing
        all feature columns required by the risk scorer.
    """
    features = (
        transactions_df.groupby("account_id")
        .agg(
            account_age_days=("timestamp", lambda x: (x.max() - x.min()).days),
            avg_transaction_amount=("amount", "mean"),
            transaction_frequency=("transaction_id", "count"),
            late_payment_count=("late_payment_count", "sum"),
        )
        .reset_index()
    )

    # Credit utilization ratio: avg amount / max amount seen for the account
    # Proxy calculation — real implementation would join against credit limit table
    max_amounts = transactions_df.groupby("account_id")["amount"].max().rename("max_amount")
    features = features.merge(max_amounts, on="account_id")
    features["credit_utilization_ratio"] = (
        features["avg_transaction_amount"] / features["max_amount"]
    ).clip(0, 1)
    features.drop(columns=["max_amount"], inplace=True)

    return features


def scale_features(features_df: pd.DataFrame) -> np.ndarray:
    """
    Apply standard scaling to the feature matrix.

    Args:
        features_df: DataFrame with columns matching FEATURE_COLUMNS.

    Returns:
        Scaled numpy array ready for model inference.
    """
    scaler = StandardScaler()
    X = features_df[FEATURE_COLUMNS].fillna(0).values
    return scaler.fit_transform(X)
