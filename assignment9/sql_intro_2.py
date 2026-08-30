import sqlite3
import pandas as pd

conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")

    query = """
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products
            ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

    print("\nFirst five rows:")
    print(df.head())

    df["total"] = df["quantity"] * df["price"]

    print("\nFirst five rows with total:")
    print(df.head())

    summary_df = df.groupby(
        "product_id",
        as_index=False
    ).agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    })

    print("\nGrouped product summary:")
    print(summary_df.head())

    summary_df = summary_df.sort_values(by="product_name")

    summary_df.to_csv("order_summary.csv", index=False)

    print("\nSorted order summary:")
    print(summary_df.head())
    print("\norder_summary.csv created successfully.")

except (sqlite3.Error, pd.errors.DatabaseError) as error:
    print(f"Database error: {error}")

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")