""" Base Component
Functions added when they have been tested and completed
"""

import easygui


# Function to display menu and welcome screen
def welcome():
    # Welcome message
    easygui.msgbox("Welcome to Monster Card Catalogue", "Welcome")

    # Enter user choice
    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Cards", "Search Catalogue",
                                             "Delete Card", "Output Catalogue",
                                             "Exit"])

    # Output user choice
    return user_choice


# MAIN ROUTINE
welcome()

if welcome() == "Add Card":
    print("Add Card")

elif welcome() == "Search Catalogue":
    print("Search Catalogue")

elif welcome() == "Delete Card":
    print("Delete Card")

elif welcome() == "Output Catalogue":
    print("Output Catalogue")

elif welcome() == "Exit":
    print("Goodbye")
