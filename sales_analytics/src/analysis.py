import pandas as pd


def compute_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df["revenue"] = df["quantity"] * df["price"]
    return df


def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("region", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )


def filter_top_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    return (
        df.groupby("product", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(top_n)
    )
