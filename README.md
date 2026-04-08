
# 🚀 Automated Data Quality & Drift Monitoring System

## 📌 Overview

This project is a **production-style data monitoring system** that automatically checks dataset quality and detects data drift between datasets.

It simulates real-world data validation pipelines used in data engineering and machine learning systems.

---

## ⚙️ Features

* 📊 Data Quality Checks (missing values, statistics, outliers)
* 🔄 Data Drift Detection between reference and new datasets
* 🌐 FastAPI-based backend for automated analysis
* 📈 Interactive Streamlit dashboard for visualization
* 🚀 End-to-end pipeline from data ingestion to reporting

---

## 🧱 Architecture

Data Upload → Quality Checks → Drift Detection → API → Dashboard

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* FastAPI (Backend API)
* Streamlit (Dashboard UI)
* Plotly (Visualization)

---

## 🚀 How to Run

```bash
# Install required libraries
pip install fastapi uvicorn streamlit python-multipart plotly

# Run API
python -m uvicorn src.app:app --reload

# Run Dashboard
python -m streamlit run src/dashboard.py
```

---

## 📊 Key Highlights

* Built a complete end-to-end system, not just scripts
* Combined data validation + drift detection in one pipeline
* Designed a backend API for automated processing
* Developed a user-friendly dashboard for real-time insights
* Focused on clean architecture and modular design

---

## 🔮 Future Improvements

* Real-time streaming (Kafka integration)
* Advanced ML-based drift detection
* Deployment using Docker

---

