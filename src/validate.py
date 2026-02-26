import pandas as pd

def validate_data(df: pd.DataFrame):

    assert df["order_id"].notnull().all(), "Null order_id found"
    assert (df["quantity"] > 0).all(), "Negative quantity detected"
    assert (df["price"] > 0).all(), "Invalid price detected"

    allowed_status = ["paid", "pending", "failed"]
    assert df["payment_status"].isin(allowed_status).all(), "Invalid payment_status"

    duplicates = df.duplicated(subset=["order_id"]).sum()
    assert duplicates == 0, "Duplicate order_id detected"

    print("Validation passed")
