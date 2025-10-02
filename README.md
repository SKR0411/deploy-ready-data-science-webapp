# Deploy-ready Data Science Web App

This is a starter template for deploying a data science web application using FastAPI.

## Quickstart (local)

1. Create virtualenv and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt

2. Train model:

   python backend/train/train_model.py

3. Run locally with uvicorn:

   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

4. Open http://localhost:8000

## Docker

1. Build image (after training and model.joblib exists):
   docker build -t ds-app ./backend
2. Run with docker-compose:
   docker-compose up --bui