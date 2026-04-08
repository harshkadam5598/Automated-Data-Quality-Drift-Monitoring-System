
import pandas as pd


# 🔹 Load datasets
def load_data(reference_path, current_path):
    ref_df = pd.read_csv(reference_path, encoding="latin1")
    curr_df = pd.read_csv(current_path, encoding="latin1")

    print("[INFO] Reference and current data loaded")

    return ref_df, curr_df


# 🔹 Drift detection (mean difference)
def detect_drift(ref_df, curr_df):
    drift_report = {}

    numeric_cols = ref_df.select_dtypes(include=["float64", "int64"]).columns

    for col in numeric_cols:
        ref_mean = ref_df[col].mean()
        curr_mean = curr_df[col].mean()

        diff = abs(curr_mean - ref_mean)

        drift_report[col] = {
            "reference_mean": float(round(ref_mean, 2)),
            "current_mean": float(round(curr_mean, 2)),
            "difference": float(round(diff, 2)),
            "drift_detected": bool(diff > (0.2 * ref_mean))  # 20% threshold
        }

    print("[INFO] Drift detection completed")

    return drift_report


# 🔹 Run standalone
if __name__ == "__main__":
    ref, curr = load_data("../data/reference_data.csv", "../data/sample_data.csv")
    report = detect_drift(ref, curr)

    print("\n=== DRIFT REPORT ===")
    for col, details in report.items():
        print(f"{col}: {details}")

