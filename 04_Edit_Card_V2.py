"""Component 4 Version 2, Edit Card,
Trial 1 using a function, also trial 1 part 2 using an enterbox"""

import easygui


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
            break
        else:
            change_value = easygui.buttonbox("What would you like to change?",
                                             "Change Choice",
                                             choices=["Power Value",
                                                      "Card Name"])

            if change_value == "Power Value":
                current_value = easygui.enterbox("Enter the name of the power "
                                                 "you wish to change the "
                                                 "value of:", "Power Value")\
                    .title()
                if current_value not in confirm_card[card_name]:
                    easygui.msgbox("Sorry, that is not the name of "
                                   "a power on this card:\n\n"
                                   f"{title}\n" f"{card}", "Error")

                    current_value = easygui.enterbox(
                        "Enter the name of the power "
                        "you wish to change the "
                        "value of:", "Power Value")

                else:
                    new = easygui.integerbox(
                        f"Enter the value you want to change"
                        f" {current_value} to:", "New Value")

                    confirm_card[card_name][current_value] = new

            if change_value == "Card Name":
                new = easygui.enterbox(f"Enter the name you want to change "
                                       f"{card_name} to:", "New Name").title()
                confirm_card[new] = confirm_card.pop(card_name)
                print(confirm_card)

        correct = easygui.buttonbox(f"Is the following card correct?\n"
                                    f"{title}\n" f"{card}", "Card Check",
                                    choices=["Yes", "No"])


# Main routine
cards = {"Stoneling":
         {"Strength": 7, "Speed": 1,
          "Stealth": 25, "Cunning": 15}}

edit(cards)
print(cards)
