"""Component 5 Version 5, Search Card, builds on the code from version 4,
now in a loop so the user can try and enter again if card not found in
catalogue"""

import easygui


# Blank checker function
def blank_check(question, title, box):
    error = "Please answer all questions"
    while True:
        # Enter-box
        if box == "enter":
            # Ask for input
            response = easygui.enterbox(question, title)

            # If cancel is pressed
            if not response:
                easygui.msgbox(error, "Error")

            # If valid response
            else:
                return response

        else:
            # Ask for input
            response = easygui.integerbox(question, title, upperbound=25,
                                          lowerbound=0)

            # If cancel is pressed
            if not response:
                easygui.msgbox(error, "Error")

            # If valid response
            else:
                return response


# Function to confirm and edit cards
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
            easygui.msgbox(f"You have successfully entered the new card "
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
            if new in confirm_card:
                new = blank_check(f"Sorry that name already is already taken!"
                                  f"Enter the name you want to change "
                                  f"{card_name} to:", "New Name",
                                  "enter").title()
            confirm_card[new] = confirm_card.pop(card_name)


catalogue = {"Stoneling":
                 {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
             "Vexscream":
                 {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
             "Dawnmirage":
                 {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}}

while True:
    # User enters card name
    search_name = easygui.enterbox("Enter name of card: ", "Search").title()

    if not search_name:
        break

    while search_name not in catalogue:
        easygui.msgbox(
            f"Sorry {search_name} is not a card in the Monster Card "
            f"catalogue", "Card Not Found")

        # User enters card name
        search_name = easygui.enterbox("Enter name of card: ", "Search").\
            title()

    # Add the searched card to separate dictionary
    searched_card = {search_name: catalogue[search_name]}

    # Confirm the searched card
    correct_card = edit(searched_card)

    # Update the catalogue
    del [catalogue[search_name]]
    catalogue.update(correct_card)
    break
