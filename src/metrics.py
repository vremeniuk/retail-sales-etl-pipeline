import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> dict:

    total_revenue = df["revenue"].sum()

    revenue_per_category = (
        df.groupby("category")["revenue"]
        .sum()
        .to_dict()
    )

    avg_order_value = df.groupby("order_id")["revenue"].sum().mean()

    paid_revenue = df[df["is_paid"] == 1]["revenue"].sum()

    monthly_revenue = (
        df.groupby("order_month")["revenue"]
        .sum()
        .sort_index()
    )

    monthly_growth = monthly_revenue.pct_change().fillna(0).to_dict()

    return {
        "total_revenue": total_revenue,
        "revenue_per_category": revenue_per_category,
        "average_order_value": avg_order_value,
        "paid_revenue": paid_revenue,
        "monthly_growth_rate": monthly_growth
    }
