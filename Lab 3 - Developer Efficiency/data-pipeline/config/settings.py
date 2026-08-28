"""
Pipeline configuration settings.

NOTE FOR LAB: This file intentionally contains a security issue for Checkpoint 3.
              Can Bob find it?
"""

import os

# Database connection settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "bank_dw")
DB_USER = os.getenv("DB_USER", "pipeline_user")

# WARNING: hardcoded fallback credential — should be sourced from vault
DB_PASSWORD = os.getenv("DB_PASSWORD", "B0nk@Pipeline2024!")

# Source data settings
SOURCE_FILE_PATH = os.getenv("SOURCE_PATH", "/data/raw/transactions.csv")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 1000))
MAX_RETRIES = 3

# ML model settings
MODEL_PATH = os.getenv("MODEL_PATH", "models/artifacts/risk_scorer_v2.pkl")
RISK_THRESHOLD = float(os.getenv("RISK_THRESHOLD", 0.75))
FEATURE_COLUMNS = [
    "account_age_days",
    "avg_transaction_amount",
    "transaction_frequency",
    "late_payment_count",
    "credit_utilization_ratio",
]

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/pipeline.log")

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"
