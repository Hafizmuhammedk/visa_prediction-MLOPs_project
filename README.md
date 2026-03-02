# US Visa Prediction - End-to-End MLOps Project

A production-style machine learning project for **US visa case status prediction**.

This repository includes:
- data ingestion from MongoDB
- data validation and drift checks
- feature engineering and transformation
- model training, evaluation, and model pushing
- FastAPI web app for online prediction

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [API Endpoints](#api-endpoints)
- [Prediction Output](#prediction-output)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## Project Overview

The project implements a full ML lifecycle pipeline:

1. **Data Ingestion**: pulls data from MongoDB and stores it in artifact folders.
2. **Data Validation**: validates schema and checks drift.
3. **Data Transformation**: preprocesses features and handles class imbalance.
4. **Model Training**: trains and saves model artifacts.
5. **Model Evaluation**: compares/evaluates models.
6. **Model Pusher**: pushes accepted model for serving.
7. **Serving**: FastAPI app exposes UI/API for prediction.

---

## Tech Stack

- **Language**: Python
- **ML / Data**: pandas, scikit-learn, imbalanced-learn
- **Backend**: FastAPI, Uvicorn
- **Templating/UI**: Jinja2, HTML, CSS
- **Database**: MongoDB
- **Config/Artifacts**: YAML + artifact directory structure

---

## Repository Structure

```text
.
├── app.py
├── demo.py
├── requirements.txt
├── config/
│   ├── model.yaml
│   └── schema.yaml
├── templates/
│   └── usvisa.html
├── static/
│   └── css/style.css
└── us_visa/
    ├── components/
    │   ├── data_ingestion.py
    │   ├── data_validation.py
    │   ├── data_transformation.py
    │   ├── model_trainer.py
    │   ├── model_evaluation.py
    │   └── model_pusher.py
    ├── pipline/
    │   ├── training_pipeline.py
    │   └── prediction_pipeline.py
    ├── entity/
    ├── configuration/
    ├── data_access/
    ├── constants/
    └── utils/
```

---

## Setup

### 1. Clone repository

```bash
git clone <your-repo-url>
cd MLOPs-Visa_Prediction
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Set required variables for MongoDB/app config before running training or inference.

---

## How to Run

### Run Training Pipeline

```bash
python3 demo.py
```

This runs ingestion -> validation -> transformation -> trainer -> evaluation -> pusher.

### Run FastAPI App

```bash
uvicorn app:app --reload
```

Open in browser:
- `http://127.0.0.1:8000`

---

## API Endpoints

### `GET /`
Renders prediction UI.

### `POST /`
Receives form inputs and returns prediction result in UI.

### `GET /train`
Triggers model training pipeline from API route.

Example:

```bash
curl http://127.0.0.1:8000/train
```

---

## Prediction Output

Current labels in the app:

- `Visa-approved`
- `Visa Not-Approved` (declined)

---

## Troubleshooting

### `python: command not found`
Use `python3` instead.

### `ModuleNotFoundError`
Install dependencies:

```bash
pip install -r requirements.txt
```

### MongoDB connection errors
- verify URI/credentials
- ensure MongoDB server is reachable
- check env variables are loaded

### No model artifact during prediction
Run training first:

```bash
python3 demo.py
```

---

## Roadmap

- Add Docker Compose for one-command local startup
- Add CI for lint/test/build
- Add unit/integration tests for pipeline components
- Add model monitoring and drift alerting dashboard
- Add API docs examples for JSON prediction route

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-change`)
3. Commit changes (`git commit -m "feat: your change"`)
4. Push branch and open a Pull Request

---

If you want, I can also add a **deployment section** (Render/EC2/GCP/Azure) and a **badges header** for GitHub.
