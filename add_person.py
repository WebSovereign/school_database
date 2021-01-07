import sqlite3


def add_person():

    # Create a connection to sqlite3
    # Try to connect to a database called 'school.db'
    # If 'school.db' does not exist, create it
    conn = sqlite3.connect("school.db")

    # Create a cursor to make queries with
    c = conn.cursor()

    # Ask user to enter information about the new person
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    email = input("Please enter email: ")
    phone = input("Please enter phone: ")
    position = input("Please enter position: ")

    c.execute("INSERT INTO people VALUES (?, ?, ?, ?, ?);",
              (first_name, last_name, email, phone, position))

    conn.commit()

    conn.close()

    print(f"{first_name} {last_name} added to the school database.")
