import sqlite3


def print_data():
    conn = sqlite3.connect("school.db")

    c = conn.cursor()

    c.execute("SELECT * FROM people")
    people = c.fetchall()

    for person in people:
        print(person)

    conn.commit()

    conn.close()
