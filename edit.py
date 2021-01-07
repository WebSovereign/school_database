import sqlite3


def edit_person():
    first_name = input("Enter their first name: ")
    last_name = input("Enter their last name: ")

    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    choice = ""

    while (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"):

        print("1. First name")
        print("2. Last name")
        print("3. Email")
        print("4. Phone")
        print("5. Position")
        print("What do you want to edit about this person:")

        choice = input()

        if (choice == "1"):
            new_first_name = input("Enter new first name: ")

            # Update the database
            c.execute("""
                UPDATE people
                SET first_name = (?) WHERE first_name = (?) AND last_name = (?)
            """, (new_first_name, first_name, last_name))

        elif (choice == "2"):
            new_last_name = input("Enter new last name: ")

            # Update the database
            c.execute("""
                UPDATE people
                SET last_name = (?) WHERE first_name = (?) AND last_name = (?)
            """, (new_last_name, first_name, last_name))

        elif (choice == "3"):
            new_email = input("Enter new email: ")

            # Update the database
            c.execute("""
                UPDATE people
                SET email = (?) WHERE first_name = (?) AND last_name = (?)
            """, (new_email, first_name, last_name))

        elif (choice == "4"):
            new_phone = input("Enter new phone: ")

            # Update the database
            c.execute("""
                UPDATE people
                SET phone = (?) WHERE first_name = (?) AND last_name = (?)
            """, (new_phone, first_name, last_name))

        elif (choice == "5"):
            new_position = input("Enter new position: ")

            # Update the database
            c.execute("""
                UPDATE people
                SET position = (?) WHERE first_name = (?) AND last_name = (?)
            """, (new_position, first_name, last_name))

        else:
            print("Please enter a 1-5")

    conn.commit()
    conn.close()
