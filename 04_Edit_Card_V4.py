"""Component 4 Version 4, Edit Card
Second Version of trialling, using button boxes not an enter-box """

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
                current_value = easygui.buttonbox(
                    "Please click the box of the "
                    "power you want to change: ",
                    "Power Choice", choices=[
                        "Strength", "Speed", "Stealth", "Cunning"])

                if current_value == "Strength":
                    new = easygui.integerbox(
                        f"Enter the value you want to change"
                        f" {current_value} to:", "New Value")

                    confirm_card[card_name][current_value] = new

                elif current_value == "Speed":
                    new = easygui.integerbox(
                        f"Enter the value you want to change"
                        f" {current_value} to:", "New Value")

                    confirm_card[card_name][current_value] = new

                elif current_value == "Stealth":
                    new = easygui.integerbox(
                        f"Enter the value you want to change"
                        f" {current_value} to:", "New Value")

                    confirm_card[card_name][current_value] = new

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
