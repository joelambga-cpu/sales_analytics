import pandas as pd
import matplotlib.pyplot as plt


def plot_revenue_by_region(df: pd.DataFrame) -> None:
    revenue_by_region = (
        df.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    revenue_by_region.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()
