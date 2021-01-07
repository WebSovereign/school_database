import sqlite3


def delete_person():
    # Connect to school database
    conn = sqlite3.connect("school.db")
    c = conn.cursor()

    # Ask user to verify who they want deleted from database
    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    c.execute("DELETE FROM people WHERE first_name = (?) AND last_name = (?)",
              (first_name, last_name))

    print(f"{first_name} {last_name} has been deleted from the school database.")

    conn.commit()
    conn.close()
