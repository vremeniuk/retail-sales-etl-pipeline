import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["quantity"] = df["quantity"].fillna(1)
    df = df[df["quantity"] > 0]

    df["category"] = df["category"].str.strip().str.title()

    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["revenue"] = df["quantity"] * df["price"]
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["is_paid"] = df["payment_status"].apply(lambda x: 1 if x == "paid" else 0)

    return df
