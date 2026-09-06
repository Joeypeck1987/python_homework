import sqlite3


# Task 1: Complex JOINs with Aggregation
def main():
    # Run this program from python_homework/assignment10.
    # Read-only mode prevents creating an empty database if the path is wrong.
    connection = sqlite3.connect("file:../db/lesson.db?mode=ro", uri=True)
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT orders.order_id,
                   SUM(products.price * line_items.quantity) AS total_price
            FROM orders
            JOIN line_items ON orders.order_id = line_items.order_id
            JOIN products ON line_items.product_id = products.product_id
            GROUP BY orders.order_id
            ORDER BY orders.order_id
            LIMIT 5;
        """)

        for order_id, total_price in cursor.fetchall():
            print(f"Order ID: {order_id}, Total price: ${total_price:.2f}")

                    # Task 2: Understanding Subqueries
        print("\nTask 2: Average order price per customer")

        cursor.execute("""
            SELECT customers.customer_name,
                   AVG(order_totals.total_price) AS average_total_price
            FROM customers
            LEFT JOIN (
                SELECT orders.customer_id AS customer_id_b,
                       SUM(products.price * line_items.quantity) AS total_price
                FROM orders
                JOIN line_items
                    ON orders.order_id = line_items.order_id
                JOIN products
                    ON line_items.product_id = products.product_id
                GROUP BY orders.order_id, orders.customer_id
            ) AS order_totals
                ON customers.customer_id = order_totals.customer_id_b
            GROUP BY customers.customer_id, customers.customer_name
            ORDER BY customers.customer_id;
        """)

        for customer_name, average_total_price in cursor.fetchall():
            if average_total_price is None:
                print(f"{customer_name}: No order total available")
            else:
                print(f"{customer_name}: ${average_total_price:.2f}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
