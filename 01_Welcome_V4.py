"""Component 1, Version 4, Welcome Screen
Based off 01_Welcome_V3 but has now been made into a function """

import easygui


# Welcome screen function
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


# Main Routine
option = welcome()
print(f"You entered {option}")
