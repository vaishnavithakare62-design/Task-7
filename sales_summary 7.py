import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales_data.db"  # keep DB in the same folder as this script

def main():
    conn = sqlite3.connect(DB_PATH)

    query_per_product = """
    SELECT 
      product_name, 
      SUM(quantity) AS total_qty, 
      ROUND(SUM(quantity * price), 2) AS revenue
    FROM sales
    GROUP BY product_name
    ORDER BY revenue DESC;
    """

    query_overall = """
    SELECT 
      SUM(quantity) AS total_qty_all, 
      ROUND(SUM(quantity * price), 2) AS revenue_all
    FROM sales;
    """

    df = pd.read_sql_query(query_per_product, conn)
    totals = pd.read_sql_query(query_overall, conn)
    conn.close()

    # Print results
    print("Per-Product Summary:")
    print(df.to_string(index=False))
    print("\nOverall Totals:")
    print(totals.to_string(index=False))

    # Plot revenue by product
    plt.figure()
    plt.bar(df["product_name"], df["revenue"])
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.show()

if __name__ == "__main__":
    main()