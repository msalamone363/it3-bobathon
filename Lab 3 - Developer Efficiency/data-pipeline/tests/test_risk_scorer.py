"""
Tests for models/risk_scorer.py

Covers flag_high_risk logic.
Checkpoint 6 participants: these tests are safe to run without a real model artifact.
The model-loading path (score_accounts) requires a .pkl file — see the Checkpoint 6
instructions for how to run Bob Findings analysis on that function instead.
"""

import pytest
import numpy as np
from models.risk_scorer import flag_high_risk


def test_flag_high_risk_marks_scores_above_threshold():
    scores = np.array([0.2, 0.6, 0.8, 0.95])
    result = flag_high_risk(scores, threshold=0.75)
    assert result.tolist() == [False, False, True, True]


def test_flag_high_risk_marks_exact_threshold_as_high_risk():
    scores = np.array([0.75])
    result = flag_high_risk(scores, threshold=0.75)
    assert result[0] is np.bool_(True)


def test_flag_high_risk_all_low_scores():
    scores = np.array([0.1, 0.2, 0.3])
    result = flag_high_risk(scores, threshold=0.75)
    assert not result.any()


def test_flag_high_risk_all_high_scores():
    scores = np.array([0.8, 0.9, 1.0])
    result = flag_high_risk(scores, threshold=0.75)
    assert result.all()


def test_flag_high_risk_empty_array():
    scores = np.array([])
    result = flag_high_risk(scores, threshold=0.75)
    assert len(result) == 0
