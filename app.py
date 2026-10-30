
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

# Compatibility fix: restore _RemainderColsList for pipelines pickled with scikit-learn 1.6
import sklearn.compose._column_transformer as ct
if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    ct._RemainderColsList = _RemainderColsList

from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best_pipeline.joblib" if (BASE_DIR / "models" / "best_pipeline.joblib").exists() else BASE_DIR / "best_pipeline.joblib"
TEMPLATE_PATH = BASE_DIR / "templates" / "index.html" if (BASE_DIR / "templates" / "index.html").exists() else BASE_DIR / "index.html"

app = FastAPI(title="Walmart Sales Predictive API", version="1.0.0")
pipeline = joblib.load(MODEL_PATH)

class PredictionPayload(BaseModel):
    Store: float
    Holiday_Flag: float
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    Date: str

@app.get("/")
def index():
    return FileResponse(TEMPLATE_PATH)

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": "RandomForest"}

@app.post("/predict")
def predict(payload: PredictionPayload):
    data = pd.DataFrame([payload.model_dump()])
    pred = pipeline.predict(data)[0]
    return {"prediction": float(pred)}
