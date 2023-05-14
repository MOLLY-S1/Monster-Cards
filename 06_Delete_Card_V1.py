"""Component 6 Version 1, Delete Card"""
import easygui

# Combo Menu
catalogue = {"Stoneling":
             {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
             "Vexscream":
                 {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
             "Dawnmirage":
                 {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}}

cards = ""

# loop to print dictionary
for card_name, card_info in catalogue.items():

    # Combo name printed
    name += f"\n{card_name}\n"

    # Loop to print dictionary inside the dictionary
    for key, value in combo_info.items():
        # Combo item and its price printed
        menu += f"{key}: ${value} \n"

# User enters combo name
choice = easygui.enterbox(f"Below is the full combo menu:\n\n"
                          f"{menu}\n\n"
                          f"What would you like to delete:", "Delete Combo").upper()

while choice not in combos:
    easygui.msgbox(f"Sorry, {choice} is not in the combo menu")

    # User enters combo name
    choice = easygui.enterbox(f"Below is the full combo menu:\n\n"
                              f"{menu}\n\n"
                              f"What would you like to delete:",
                              "Delete Combo").upper()

# Add combo to menu dictionary
del [combos[choice]]
easygui.msgbox(f"{choice} has been deleted from the menu")
