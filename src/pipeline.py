import os
import logging
from extract import extract_data
from transform import clean_data, transform_data
from validate import validate_data
from metrics import calculate_metrics


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


RAW_PATH = "data/raw/sales_raw.csv"
CLEAN_PATH = "data/cleaned/sales_cleaned.csv"
ANALYTICS_PATH = "data/analytics/sales_analytics.csv"


def run_pipeline():

    logger.info("Extracting data...")
    df = extract_data(RAW_PATH)

    logger.info("Cleaning data...")
    df = clean_data(df)

    logger.info("Validating data...")
    validate_data(df)

    logger.info("Transforming data...")
    df = transform_data(df)

    logger.info("Saving cleaned data...")
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)

    logger.info("Calculating metrics...")
    metrics = calculate_metrics(df)

    logger.info("Saving analytics dataset...")
    os.makedirs("data/analytics", exist_ok=True)
    df.to_csv(ANALYTICS_PATH, index=False)

    logger.info("Pipeline completed successfully 🚀")

    for key, value in metrics.items():
        logger.info(f"{key}: {value}")


if __name__ == "__main__":
    run_pipeline()
