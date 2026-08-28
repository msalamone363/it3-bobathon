# Truist Data Pipeline — Sample Repository

Welcome to the `truist-data-pipeline` sample project. This is a simplified Python data engineering
codebase built for the Truist Bob-a-thon lab exercises.

## What's in this repo

```
truist-data-pipeline/
├── README.md                     ← You are here
├── requirements.txt              ← Python dependencies
├── config/
│   └── settings.py               ← Pipeline configuration (environment, credentials)
├── pipeline/
│   ├── __init__.py
│   ├── ingest.py                 ← Data ingestion from source systems
│   ├── transform.py              ← Data transformation and cleaning
│   ├── validate.py               ← Data quality validation
│   └── loader.py                 ← Load transformed data to destination
├── models/
│   ├── __init__.py
│   ├── risk_scorer.py            ← ML model: credit risk scoring
│   └── feature_engineering.py   ← Feature extraction for ML models
├── utils/
│   ├── __init__.py
│   ├── logger.py                 ← Logging utilities
│   └── db.py                     ← Database connection helpers
└── tests/
    ├── __init__.py
    ├── test_ingest.py            ← Ingest tests (missing file, missing columns, empty file)
    ├── test_transform.py         ← Transform tests (includes planted bug regression test)
    ├── test_validate.py          ← Validation tests
    └── test_risk_scorer.py       ← Risk scorer tests (flag_high_risk logic)
```

## Setup

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest tests/
```

## Bob installation

Bob should already be running in your TechZone VM.  
If you need to verify: open a terminal in Bob and run `bob --version`.

See `resources/bob-installation.md` in the bobathon materials for full setup instructions.

---

**Questions?** Contact Madison Ramsey — madison.ramsey@ibm.com
