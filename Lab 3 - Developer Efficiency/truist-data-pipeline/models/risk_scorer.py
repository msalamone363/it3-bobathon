"""
Credit risk scoring model.

Loads a pre-trained scikit-learn model and scores accounts based on
their engineered feature vectors. Used by downstream risk reporting pipelines.

NOTE FOR LAB (Checkpoint 6 — Bob Findings):
  This module has several ML code quality issues for Bob Findings to surface:
  - Model is loaded from disk on every call (no caching)
  - No input validation on feature array shape
  - predict_proba threshold hardcoded as a magic number
  - No logging of prediction distribution for monitoring
"""

import numpy as np
import pickle
import logging
from config.settings import MODEL_PATH, RISK_THRESHOLD

logger = logging.getLogger(__name__)


def load_model(model_path: str = MODEL_PATH):
    """
    Load the serialized risk scoring model from disk.

    Note: Called on every score_accounts invocation — no caching.
          This is intentionally inefficient for the Bob Findings exercise.
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    logger.info(f"Loaded risk model from {model_path}")
    return model


def score_accounts(feature_matrix: np.ndarray) -> np.ndarray:
    """
    Score a batch of accounts and return risk probabilities.

    Args:
        feature_matrix: 2D numpy array of shape (n_accounts, n_features).
                        Must match the feature order in FEATURE_COLUMNS.

    Returns:
        1D array of risk scores in [0, 1] for each account.
    """
    # Model loaded from disk on every call — no caching (intentional for Findings exercise)
    model = load_model()
    probabilities = model.predict_proba(feature_matrix)[:, 1]
    return probabilities


def flag_high_risk(scores: np.ndarray, threshold: float = RISK_THRESHOLD) -> np.ndarray:
    """
    Return a boolean array indicating which accounts exceed the risk threshold.

    Args:
        scores: Array of risk probabilities from score_accounts.
        threshold: Probability above which an account is flagged as high-risk.
                   Defaults to RISK_THRESHOLD from settings (0.75).

    Returns:
        Boolean array — True where risk score >= threshold.
    """
    return scores >= threshold  # magic number pattern: threshold could be logged
