""" Base Component
Functions added when they have been tested and completed
"""

import easygui


# Function to display menu and welcome screen
def welcome():
    # Enter user choice
    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Cards", "Search Catalogue",
                                             "Delete Card", "Output Catalogue",
                                             "Exit"])

    # Output user choice
    return user_choice


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


# Edit card function
def edit(confirm_card):
    while True:
        card = ""
        for card_name, card_info in confirm_card.items():
            title = f"\nCard Name: {card_name}"
            for key, value in card_info.items():
                card += f"{key}: {value}\n"

        correct = easygui.buttonbox(f"Is the following card correct?\n"
                                    f"{title}\n" f"{card}", "Card Check",
                                    choices=["Yes", "No"])

        if correct == "Yes":
            easygui.msgbox(f"You have sucessfully entered the new card "
                           f"{card_name} to the Monster Cards Catalogue",
                           "Card added")
            return confirm_card

        change_value = easygui.buttonbox("What would you like to change?",
                                         "Change Choice",
                                         choices=["Power Value",
                                                  "Card Name", ])

        if change_value == "Power Value":
            current_value = blank_check("Enter the name of the power "
                                        "which value you wish to "
                                        "change:", "Power Name",
                                        "enter").title()

            while current_value not in confirm_card[card_name]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an power in this card:\n\n"
                               f"{title}\n" f"{card}", "Error")

                current_value = blank_check("Enter the name of the "
                                            "power which value you wish "
                                            "to change:", "Power Name",
                                            "enter").title()

            new = blank_check(f"Enter the value you want to change"
                              f" {current_value} to:", "New Value",
                              "integer")

            confirm_card[card_name][current_value] = new

        elif change_value == "Card Name":
            new = blank_check(f"Enter the name you want to change "
                              f"{card_name} to:", "New Name", "enter").title()
            confirm_card[new] = confirm_card.pop(card_name)


# Add card function
def add_card():
    # Dictionary for new cards to be added and edited from
    new_cards = {}

    # User enters power values
    name = blank_check("Enter Card Name:", "Card Name", "enter")
    strength = blank_check("Enter Strength Value:", "Strength",
                           "integer")
    speed = blank_check("Enter Speed Value:", "Speed", "integer")
    stealth = blank_check("Enter Stealth Value:", "Stealth", "integer")
    cunning = blank_check("Enter Cunning Value:", "Cunning", "integer")

    # Add the values to the dictionary
    new_cards[name] = {}
    new_cards[name]["Strength"] = strength
    new_cards[name]["Speed"] = speed
    new_cards[name]["Stealth"] = stealth
    new_cards[name]["Cunning"] = cunning

    correct_card = edit(new_cards)
    catalogue.update(correct_card)


# Function to search catalogue for card
def search_card():
    while True:
        # User enters card name
        search_name = blank_check("Enter name of card: ", "Search",
                                  "enter").title()

        while search_name not in catalogue:
            easygui.msgbox(
                f"Sorry {search_name} is not a card in the Monster Card "
                f"catalogue", "Card Not Found")

            # User enters card name
            search_name = blank_check("Enter name of card: ", "Search",
                                      "enter").title()

        # Add the searched card to separate dictionary
        searched_card = {search_name: catalogue[search_name]}

        # Confirm the searched card
        correct_card = edit(searched_card)

        # Update the catalogue
        del [catalogue[search_name]]
        catalogue.update(correct_card)
        break


# MAIN ROUTINE

catalogue = {"Stoneling":
             {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
             "Vexscream":
                 {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
             "Dawnmirage":
                 {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
             "Blazegolem":
                 {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
             "Websnake":
                 {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
             "Moldvine":
                 {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
             "Vortexwing":
                 {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
             "Rotthing":
                 {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
             "Froststep":
                 {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
             "Wispghoul":
                 {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
             }

# Welcome message
easygui.msgbox("Welcome to Monster Card Catalogue", "Welcome")
choice = welcome()

while choice != "Exit":
    if choice == "Add Cards":
        add_card()
        choice = welcome()

    elif choice == "Search Catalogue":
        search_card()
        choice = welcome()

    elif choice == "Delete Card":
        print("Delete Card")
        choice = welcome()

    elif choice == "Output Catalogue":
        print("Output Catalogue")
        choice = welcome()

easygui.msgbox("Goodbye", "Goodbye")
