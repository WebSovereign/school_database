from greeting import greetUser
from add_person import add_person
from database import create_database
from print_data import print_data
from edit import edit_person
import os
os.system("clear")

# create_database()

choice = ""

while(choice != "0"):
    choice = greetUser()

    if (choice == "1"):
        add_person()
    elif (choice == "2"):
        print_data()
    elif (choice == "3"):
        edit_person()
