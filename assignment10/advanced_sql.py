import sqlite3


# Task 1: Complex JOINs with Aggregation
def main():
    # Run this program from python_homework/assignment10.
    # Open the existing database for reading and writing.
    connection = sqlite3.connect("file:../db/lesson.db?mode=rw", uri=True)
    connection.execute("PRAGMA foreign_keys = 1")
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

        # Task 3: An Insert Transaction Based on Data
        with connection:
            connection.execute("BEGIN")

            cursor.execute(
                "SELECT customer_id FROM customers WHERE customer_name = ?",
                ("Perez and Sons",)
            )
            customer_id = cursor.fetchone()[0]

            cursor.execute("""
                SELECT product_id
                FROM products
                ORDER BY price, product_id
                LIMIT 5
            """)
            products = cursor.fetchall()

            if len(products) != 5:
                raise ValueError("Five products are required for this order.")

            cursor.execute("""
                SELECT employee_id
                FROM employees
                WHERE first_name = ? AND last_name = ?
            """, ("Miranda", "Harris"))
            employee_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, date('now'))
                RETURNING order_id
            """, (customer_id, employee_id))
            order_id = cursor.fetchall()[0][0]

            cursor.executemany("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, [
                (order_id, product_id, 10)
                for (product_id,) in products
            ])

        print(f"\nTask 3: Line items for new order {order_id}")

        cursor.execute("""
            SELECT line_items.line_item_id,
                   line_items.quantity,
                   products.product_name
            FROM line_items
            JOIN products
                ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?
            ORDER BY line_items.line_item_id
        """, (order_id,))

        for line_item_id, quantity, product_name in cursor.fetchall():
            print(
                f"Line item ID: {line_item_id}, "
                f"Quantity: {quantity}, Product: {product_name}"
            )

        # Task 4: Aggregation with HAVING
        print("\nTask 4: Employees with more than 5 orders")

        cursor.execute("""
            SELECT employees.employee_id,
                   employees.first_name,
                   employees.last_name,
                   COUNT(orders.order_id) AS order_count
            FROM employees
            JOIN orders
                ON employees.employee_id = orders.employee_id
            GROUP BY employees.employee_id,
                     employees.first_name,
                     employees.last_name
            HAVING COUNT(orders.order_id) > 5
            ORDER BY employees.employee_id;
        """)

        for employee_id, first_name, last_name, order_count in cursor.fetchall():
            print(
                f"Employee ID: {employee_id}, "
                f"Name: {first_name} {last_name}, Orders: {order_count}"
            )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
