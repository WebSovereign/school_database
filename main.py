from greeting import greetUser
from add_person import add_person
from database import create_database
import os
os.system("clear")

# create_database()

choice = greetUser()

if (choice == "1"):
    add_person()
