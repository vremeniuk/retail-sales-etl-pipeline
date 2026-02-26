import os
from extract import extract_data
from transform import clean_data, transform_data
from validate import validate_data
from metrics import calculate_metrics


RAW_PATH = "data/raw/sales_raw.csv"
CLEAN_PATH = "data/cleaned/sales_cleaned.csv"
ANALYTICS_PATH = "data/analytics/sales_analytics.csv"


def run_pipeline():

    print("Extracting data...")
    df = extract_data(RAW_PATH)

    print("Cleaning data...")
    df = clean_data(df)

    print("Validating data...")
    validate_data(df)

    print("Transforming data...")
    df = transform_data(df)

    print("Saving cleaned data...")
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)

    print("Calculating metrics...")
    metrics = calculate_metrics(df)

    print("Saving analytics dataset...")
    os.makedirs("data/analytics", exist_ok=True)
    df.to_csv(ANALYTICS_PATH, index=False)

    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\nPipeline completed successfully 🚀")


if __name__ == "__main__":
    run_pipeline()
