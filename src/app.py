
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

from src.quality_checks import check_missing_values, basic_statistics, detect_outliers

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Data Quality Monitoring API is running"}


# 🔥 Upload and analyze dataset
@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    contents = await file.read()

    df = pd.read_csv(io.StringIO(contents.decode("latin1")))

    report = {
        "missing_values": check_missing_values(df),
        "basic_statistics": basic_statistics(df),
        "outliers": detect_outliers(df)
    }

    return report

