
import pandas as pd


# 🔹 Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    print("[INFO] Data loaded")
    return df


# 🔹 Missing values check
def check_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    print("[INFO] Missing values checked")

    return missing.to_dict()


# 🔹 Basic statistics
def basic_statistics(df):
    stats = df.describe().to_dict()

    print("[INFO] Basic statistics generated")

    return stats


# 🔹 Outlier detection (simple using IQR)
def detect_outliers(df):
    outlier_counts = {}

    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        outlier_counts[col] = len(outliers)

    print("[INFO] Outliers detected")

    return outlier_counts


# 🔹 Generate full report
def generate_report(file_path):
    df = load_data(file_path)

    report = {
        "missing_values": check_missing_values(df),
        "basic_statistics": basic_statistics(df),
        "outliers": detect_outliers(df)
    }

    print("[INFO] Report generated successfully")

    return report


# 🔹 Run standalone
if __name__ == "__main__":
    report = generate_report("../data/sample_data.csv")
    print(report)

    