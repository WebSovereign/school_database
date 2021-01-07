import sqlite3


def create_database():
    # Create a connection to sqlite3
    # Try to connect to a database called 'school.db'
    # If 'school.db' does not exist, create it
    conn = sqlite3.connect("school.db")

    # Create a cursor to make queries with
    c = conn.cursor()

    c.execute("""
        CREATE TABLE people (
            first_name text,
            last_name text,
            email text,
            phone text,
            position text
        )
    """)

    conn.commit()

    conn.close()
