# 🛒 Walmart Sales Predictor — MLOps Production Deployment

Production-ready machine learning microservice and interactive web application for forecasting weekly sales across Walmart stores. Built with **FastAPI**, **Scikit-Learn**, **Uvicorn**, and containerized with **Docker**.

---

## 📌 Project Overview

- **Task Type**: Regression
- **Target Variable**: `Weekly_Sales` (Forecasted sales in USD)
- **Model Engine**: Random Forest Regressor Pipeline (`best_pipeline.joblib`)
- **Model Performance**: $R^2 \approx 0.9357$ (93.57% variance explained)
- **Serving Stack**: FastAPI + Uvicorn + Responsive HTML5/CSS3 Web UI

---

## 📁 Project Structure

```text
walmart_mlops_production_deployment_web/
│
├── models/                         # Serialized ML models and metadata
│   ├── best_pipeline.joblib        # Pre-trained scikit-learn pipeline (Random Forest)
│   └── metadata.json               # Model metrics, task type & feature schema
│
├── templates/                      # Frontend presentation layer
│   └── index.html                  # Responsive Walmart-branded UI
│
├── mlruns/                         # MLflow experiment tracking logs
├── app.py                          # FastAPI backend application & inference service
├── requirements.txt                # Python package dependencies
├── Dockerfile                      # Production container definition
├── run_app.bat                     # 1-click Windows terminal launcher
├── .gitignore                      # Git ignore rules for venv, caches, etc.
└── README.md                       # Project documentation
```

---

## 📊 Features & Target Schema

### Target (Output)
| Variable | Type | Description |
| :--- | :--- | :--- |
| **`Weekly_Sales`** | Continuous Float | Total sales revenue for the given week ($) |

### Features (Inputs)
| Feature | Type | Range / Example | Description |
| :--- | :--- | :--- | :--- |
| **`Store`** | Numeric | `1` to `45` | Walmart store identification number |
| **`Date`** | Categorical | `"2010-02-05"` | Week date (YYYY-MM-DD) |
| **`Holiday_Flag`** | Numeric | `0` or `1` | `1` if holiday week (Super Bowl, Christmas, etc.), `0` otherwise |
| **`Temperature`** | Numeric | `42.31` | Average temperature in store region (°F) |
| **`Fuel_Price`** | Numeric | `2.572` | Regional cost of fuel ($/gallon) |
| **`CPI`** | Numeric | `211.096` | Consumer Price Index (inflation metric) |
| **`Unemployment`** | Numeric | `8.106` | Regional unemployment rate percentage (%) |

---

## 🚀 Quickstart: Running via Terminal

### 1. Using Existing Environment
```powershell
cd d:\Downloads\walmart_mlops_production_deployment_web
.\.venv\Scripts\Activate.ps1
python -m uvicorn app:app --reload
```

### 2. 1-Click Launch (Windows)
Double-click [`run_app.bat`](run_app.bat) or run:
```powershell
.\run_app.bat
```

### 3. Open in Browser
- **Frontend Web UI**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 🔌 API Endpoints

### 1. Health Check
`GET /health`
```json
{
  "status": "healthy",
  "model": "RandomForest"
}
```

### 2. Predict Sales
`POST /predict`

**Request Body:**
```json
{
  "Store": 1,
  "Holiday_Flag": 0,
  "Temperature": 42.31,
  "Fuel_Price": 2.572,
  "CPI": 211.096,
  "Unemployment": 8.106,
  "Date": "2010-02-05"
}
```

**Response:**
```json
{
  "prediction": 1580625.4728
}
```

**PowerShell Example:**
```powershell
$body = @{
    Store = 1.0
    Holiday_Flag = 0.0
    Temperature = 42.31
    Fuel_Price = 2.572
    CPI = 211.096
    Unemployment = 8.106
    Date = "2010-02-05"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/predict" -Method Post -ContentType "application/json" -Body $body
```

---

## 🐳 Docker Deployment

To build and run in an isolated Docker container:

```bash
docker build -t walmart-sales-api .
docker run -d -p 8000:8000 --name walmart-api walmart-sales-api
```
Access the application at [http://localhost:8000](http://localhost:8000).

