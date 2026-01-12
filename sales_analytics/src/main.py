from src.data_loader import load_data
from src.analysis import compute_revenue, revenue_by_region
from src.visualization import plot_revenue_by_region

def main() -> None:
    df = load_data("data/sales_data.csv")
    df = compute_revenue(df)

    summary = revenue_by_region(df)
    plot_revenue_by_region(summary)

    summary.to_excel("reports/sales_summary.xlsx", index=False)
    print("Sales analytics report generated successfully!")

if __name__ == "__main__":
    main()
