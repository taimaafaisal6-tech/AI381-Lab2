from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"

FEATURES = [
    "tenure_months",
    "monthly_charges",
    "contract",
    "internet_service",
    "support_calls",
]

app = FastAPI(title="AI381 Churn Prediction API")

model = joblib.load(MODEL_PATH)


class Customer(BaseModel):
    tenure_months: float
    monthly_charges: float
    contract: str
    internet_service: str
    support_calls: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):
    data = customer.model_dump()
    X = pd.DataFrame([data])[FEATURES]

    probability = float(model.predict_proba(X)[0, 1])

    return {"churn_probability": round(probability, 3)} 