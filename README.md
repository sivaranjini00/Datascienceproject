## 📊 Data Science Project


## 📌 Project Overview

This project is an end-to-end Machine Learning pipeline designed using a modular architecture.
It automates the complete ML lifecycle from data collection to model training and evaluation, while ensuring trackability, scalability, and reproducibility.

The pipeline is built following MLOps best practices and integrates with MLflow and DagsHub for experiment tracking.

## ✨ Key Highlights

🧠 End-to-End ML Workflow — Data ingestion → validation → transformation → training → evaluation

⚡ Modular Code Structure — Separate reusable components for each pipeline stage

⚙️ Config-Driven Approach — Controlled using config.yaml, schema.yaml, and params.yaml

📂 Artifacts Management — Intermediate outputs stored in dedicated artifact folders

📈 Experiment Tracking — MLflow integrated with DagsHub for model versioning and metric logging

📦 Reproducible Pipelines — Easy to reproduce runs using main.py

🧪 Test/Train Split & Evaluation Metrics — Standard evaluation pipeline for comparing models

## 🗂 Project Structure
'''text
Datascienceproject/
│
├── config/
│   ├── config.yaml
│   ├── schema.yaml
│   └── params.yaml
│
├── src/
│   └── Datascienceproject/
│       ├── components/           # Data Ingestion, Validation, Transformation, Training, Evaluation logic
│       ├── config/               # Configuration manager classes
│       ├── entity/                # Entity dataclasses for structured configs
│       ├── pipeline/              # Orchestrating pipelines for each stage
│       ├── utils/                  # Utility/helper functions
│       └── logger.py
│
├── artifacts/                     # Generated data, models, and reports
│
├── main.py                         # Entry point to run full pipeline
├── README.md
└── requirements.txt
