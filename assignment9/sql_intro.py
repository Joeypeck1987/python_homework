import sqlite3


def add_publisher(cursor, name):
    try:
        cursor.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?",
            (name,)
        )
        publisher = cursor.fetchone()

        if publisher:
            print(f"Publisher already exists: {name}")
            return publisher[0]

        cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding publisher {name}: {error}")
        return None


def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "SELECT magazine_id FROM magazines WHERE name = ?",
            (name,)
        )
        magazine = cursor.fetchone()

        if magazine:
            print(f"Magazine already exists: {name}")
            return magazine[0]

        cursor.execute(
            """
            INSERT INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding magazine {name}: {error}")
        return None


def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT subscriber_id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )
        subscriber = cursor.fetchone()

        if subscriber:
            print(f"Subscriber already exists: {name}, {address}")
            return subscriber[0]

        cursor.execute(
            """
            INSERT INTO subscribers (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding subscriber {name}: {error}")
        return None


def add_subscription(
    cursor,
    subscriber_id,
    magazine_id,
    expiration_date
):
    try:
        cursor.execute(
            """
            SELECT subscription_id
            FROM subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
            """,
            (subscriber_id, magazine_id)
        )
        subscription = cursor.fetchone()

        if subscription:
            print("Subscription already exists.")
            return subscription[0]

        cursor.execute(
            """
            INSERT INTO subscriptions (
                subscriber_id,
                magazine_id,
                expiration_date
            )
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding subscription: {error}")
        return None


conn = None

try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id)
                REFERENCES publishers (publisher_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id)
                REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id)
                REFERENCES magazines (magazine_id),
            UNIQUE (subscriber_id, magazine_id)
        )
    """)

    # Add at least three publishers.
    publisher_1 = add_publisher(cursor, "Condé Nast")
    publisher_2 = add_publisher(cursor, "Hearst Communications")
    publisher_3 = add_publisher(cursor, "National Geographic Partners")

    # Add at least three magazines.
    magazine_1 = add_magazine(cursor, "The New Yorker", publisher_1)
    magazine_2 = add_magazine(cursor, "Esquire", publisher_2)
    magazine_3 = add_magazine(
        cursor,
        "National Geographic",
        publisher_3
    )

    # Add at least three subscribers.
    subscriber_1 = add_subscriber(
        cursor,
        "Alice Johnson",
        "100 Main Street"
    )
    subscriber_2 = add_subscriber(
        cursor,
        "Marcus Reed",
        "205 Oak Avenue"
    )
    subscriber_3 = add_subscriber(
        cursor,
        "Elena Garcia",
        "312 Pine Road"
    )

    # Add at least three subscriptions.
    add_subscription(cursor, subscriber_1, magazine_1, "2027-08-01")
    add_subscription(cursor, subscriber_2, magazine_2, "2027-09-15")
    add_subscription(cursor, subscriber_3, magazine_3, "2027-10-30")

    # Query 1: Retrieve all subscribers.
    cursor.execute("SELECT * FROM subscribers")
    subscribers = cursor.fetchall()

    print("\nAll subscribers:")
    for subscriber in subscribers:
        print(subscriber)

    # Query 2: Retrieve all magazines sorted by name.
    cursor.execute("""
        SELECT *
        FROM magazines
        ORDER BY name
    """)
    magazines = cursor.fetchall()

    print("\nMagazines sorted by name:")
    for magazine in magazines:
        print(magazine)

    # Query 3: Find magazines from a particular publisher.
    publisher_name = "Hearst Communications"

    cursor.execute("""
        SELECT magazines.magazine_id,
               magazines.name,
               publishers.name
        FROM magazines
        JOIN publishers
            ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, (publisher_name,))

    publisher_magazines = cursor.fetchall()

    print(f"\nMagazines published by {publisher_name}:")
    for magazine in publisher_magazines:
        print(magazine)

    conn.commit()
    print("Database tables and data created successfully.")

except sqlite3.Error as error:
    print(f"Database error: {error}")

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")