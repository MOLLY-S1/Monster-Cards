"""Component 6 Version 1, Delete Card"""
import easygui


# Blank checker function
def blank_check(question, title, box):
    error = "That was not a valid input\n" \
            "Please answer all questions"

    while True:
        # Enter-box
        if box == "enter":
            try:
                # Ask for input
                response = easygui.enterbox(question, title)

                # If cancel is pressed
                if not response:
                    easygui.msgbox(error, "ERROR")

                # Check if answer is given
                if response != "":
                    return response

                # Show error
                else:
                    easygui.msgbox(error, "ERROR")

            # Allow all values
            except ValueError:
                easygui.msgbox(error, "ERROR")

        # Integer-box
        elif box == "integer":
            try:
                # Ask for input
                response = easygui.integerbox(question, title,
                                              upperbound=25, lowerbound=0)

                # If cancel is pressed
                if not response:
                    easygui.msgbox(error, "ERROR")

                # Check if answer is given
                if response != "":
                    return response

                # Show error message
                else:
                    easygui.msgbox(error, "ERROR")

            # Allow all values
            except ValueError:
                easygui.msgbox(error, "ERROR")


# Card Catalogue
catalogue = {"Stoneling":
             {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
             "Vexscream":
                 {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
             "Dawnmirage":
                 {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}}

cards = ""

# loop to print dictionary
for card_name, card_info in catalogue.items():

    # Card name printed
    cards += f"\n{card_name}\n"

    # Loop to print dictionary inside the dictionary
    for key, value in card_info.items():
        # Combo item and its price printed
        cards += f"{key}: {value} \n"

# User enters card name
choice = blank_check(f"Below is the full Monster Card Catalogue:\n\n"
                     f"{cards}\n\n"
                     f"What would you like to delete:", "Delete Card",
                     "enter")

while choice not in catalogue:
    easygui.msgbox(f"Sorry, {choice} is not in the Monster Card Catalogue",
                   "Card Not Found")

    # User enters combo name
    choice = blank_check(f"Below is the full Monster Card Catalogue:\n\n"
                         f"{cards}\n\n"
                         f"What would you like to delete:",
                         "Delete Card", "enter")

# Confirm card deletion
sure = easygui.buttonbox(f"Are you sure you want to delete {choice}\n"
                         f"Once it is deleted this cannot be undone",
                         "Delete Confirm", choices=["Yes", "No"])
if sure == "Yes":
    # Remove card from catalogue dictionary
    del [catalogue[choice]]
    easygui.msgbox(f"{choice} has been deleted from the menu", "Card Removed")
