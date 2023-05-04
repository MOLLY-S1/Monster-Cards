"""Component 4 Version 4, Edit Card, now incorporates the blank checker"""

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
                                        "change:", "Power Name").title()

            while current_value not in confirm_card[card_name]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an power in this card:\n\n"
                               f"{title}\n" f"{card}", "Error")

                current_value = blank_check("Enter the name of the "
                                            "power which value you wish "
                                            "to change:", "Power Name").title()

            new = easygui.integerbox(f"Enter the value you want to change"
                                     f" {current_value} to:", "New Value",
                                     lowerbound=0, upperbound=25)

            confirm_card[card_name][current_value] = new

        elif change_value == "Card Name":
            new = blank_check(f"Enter the name you want to change "
                              f"{card_name} to:", "New Name").title()
            confirm_card[new] = confirm_card.pop(card_name)


# Main routine
cards = {"Stoneling": {
    "Strength": 7, "Speed": 1,
    "Stealth": 25, "Cunning": 15}}
edit(cards)
print(cards)
