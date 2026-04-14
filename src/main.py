import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    print("Loading export trade finance data from CSV...")
    df = pd.read_csv("../data/raw/trade_data.csv")
    return df


def summarize_data(df):
    print("Summarizing trade finance data...")

    # Calculate profit
    df["net_profit_rmb"] = (
        df["sales_amount_rmb"]
        - df["shipping_cost_rmb"]
        - df["tariff_cost_rmb"]
        - df["interest_expense_rmb"]
    )

    # Totals
    total_sales = df["sales_amount_rmb"].sum()
    total_profit = df["net_profit_rmb"].sum()

    print(f"Total sales (RMB): {total_sales}")
    print(f"Total net profit (RMB): {total_profit}")

    # Group by country (Profit)
    profit_by_country = df.groupby("country")["net_profit_rmb"].sum()

    print("\nProfit by country:")
    print(profit_by_country)

    # Best and worst country
    best_country = profit_by_country.idxmax()
    worst_country = profit_by_country.idxmin()

    print(f"\nBest market: {best_country}")
    print(f"Worst market: {worst_country}")

    # Plot 1: Profit
    plt.figure()
    profit_by_country.plot(kind="bar")

    plt.title("Profit by Country")
    plt.xlabel("Country")
    plt.ylabel("Net Profit (RMB)")

    plt.tight_layout()
    plt.savefig("../outputs/profit_by_country.png")
    plt.close()   

    # Profit Margin
    df["profit_margin"] = df["net_profit_rmb"] / df["sales_amount_rmb"]

    margin_by_country = df.groupby("country")["profit_margin"].mean()


    margin_by_country = margin_by_country * 100

    print("\nProfit margin by country:")
    print(margin_by_country)

    best_margin = margin_by_country.idxmax()
    worst_margin = margin_by_country.idxmin()

    print(f"\nHighest margin market: {best_margin}")
    print(f"Lowest margin market: {worst_margin}")

    # Plot 2: Profit Margin
    plt.figure()
    margin_by_country.plot(kind="bar")

    plt.title("Profit Margin by Country")
    plt.xlabel("Country")
    plt.ylabel("Margin (%)")


    plt.tight_layout()
    plt.savefig("../outputs/profit_margin.png")
    plt.show()


if __name__ == "__main__":
    data = load_data()
    summarize_data(data)