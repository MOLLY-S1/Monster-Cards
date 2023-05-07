"""Component 5 Version 2, Search Card, now incorporates the blank checker
function (component 2)"""

import easygui


# Blank checker function
def blank_check(question, title):
    error = "That was not a valid input\n" \
            "Please answer all questions"

    while True:
        try:
            # Ask for input
            response = easygui.enterbox(question, title)

            # Check if answer is given
            if response != "":
                return response

            else:
                easygui.msgbox(error, "ERROR")

        # Allow all values
        except ValueError:
            easygui.msgbox(error, "ERROR")


catalogue = {"Stoneling":
             {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         "Vexscream":
             {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Dawnmirage":
             {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}}

# User enters card name
search_name = blank_check("Enter name of card: ", "Search").title()

# Program outputs if card in catalogue
if search_name in catalogue:
    easygui.msgbox(f"{search_name} is a card in the monster card catalogue",
                   "Card Found")

else:
    easygui.msgbox(f"Sorry {search_name} is not a card in the monster card "
                   f"catalogue", "Card Not Found")
