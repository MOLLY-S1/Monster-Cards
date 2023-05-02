"""Component 4 Version 1, Edit Card"""

import easygui

cards = {"Stoneling":
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

while True:
    card = ""
    for card_title, card_info in cards.items():
        name = f"\nCombo Name: {card_title.upper()}"
        for key, value in card_info.items():
            card += f"{key}: {value}\n"

    correct = easygui.buttonbox(f"Is the following card correct?\n"
                                f"{name}\n" f"{card}", "Card Check",
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
                                     "Item Name")
            if power not in cards[name]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an power in this card:\n\n"
                               f"{name}\n" f"{card}", "Error")

                power = easygui.enterbox(
                    "Enter the name of the power value you "
                    "want to change \n (eg. Strength)",
                    "Item Name")

            else:
                new = easygui.integerbox(f"Enter the value you want to change"
                                         f" {power} to:", "New Value",
                                         lowerbound=0, upperbound=25)
                card[name][power] = new

        if change_value == "Combo Name":
            new = easygui.enterbox(f"Enter the name you want to change "
                                   f"{combo_ID} to:", "New Name").upper()
            confirm_combo[new] = confirm_combo.pop(combo_ID)
            print(confirm_combo)

        correct = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"{ID}\n" f"{combo}", "Combo Check",
                                    choices=["Yes", "No"])

change(combos)
print(combos)
