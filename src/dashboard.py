
import streamlit as st
import pandas as pd

from src.quality_checks import check_missing_values, basic_statistics, detect_outliers

st.set_page_config(page_title="Data Quality Monitor", layout="wide")

st.title("🚀 Data Quality & Monitoring Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    # Run checks
    missing = check_missing_values(df)
    stats = basic_statistics(df)
    outliers = detect_outliers(df)

    st.subheader("❌ Missing Values")
    st.write(missing if missing else "No missing values")

    st.subheader("📈 Basic Statistics")
    st.write(stats)

    st.subheader("⚠️ Outliers")
    st.write(outliers)

    