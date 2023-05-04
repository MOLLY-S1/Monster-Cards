"""Component 4 Version 1, Edit Card"""

import easygui

cards = {"Stoneling":
             {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}}

while True:
    card = ""
    for name, card_info in cards.items():
        card_title = f"\nCard Name: {name}"
        for key, value in card_info.items():
            card += f"{key}: {value}\n"

        correct = easygui.buttonbox(f"Is the following card correct?\n"
                                    f"{card_title}\n" f"{card}", "Card Check",
                                    choices=["Yes", "No"])

        if correct == "Yes":
            break
        else:
            change_value = easygui.buttonbox("What would you like to change?",
                                             "Change Choice",
                                             choices=["Card Name",
                                                      "Power Value"])

            if change_value == "Power Value":
                power = easygui.enterbox("Enter the name of the power value you "
                                         "want to change \n (eg. Strength)",
                                         "Item Name").title()
                if power not in cards[name]:
                    easygui.msgbox("Sorry, that is not the name of "
                                   "an power in this card:\n\n"
                                   f"{name}\n" f"{card}", "Error")

                    power = easygui.enterbox(
                        "Enter the name of the power value you "
                        "want to change \n (eg. Strength)",
                        "Item Name")

                else:
                    new = easygui.integerbox(f"Enter the value you want to "
                                             f"change {power} to:", "New Value"
                                             ,lowerbound=0, upperbound=25)
                    cards[name][power] = new

            if change_value == "Card Name":
                new = easygui.enterbox(f"Enter the name you want to change "
                                       f"{name} to:", "New Name").title()
                cards[new] = cards.pop(name)
                print(cards)

        correct = easygui.buttonbox(f"Is the following card correct?\n"
                                    f"{name}\n" f"{card}", "Card Check",
                                    choices=["Yes", "No"])
