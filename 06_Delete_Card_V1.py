"""Component 6 Version 1, Delete Card, Trial 1 using an enter-box and
showing the full catalogue"""
import easygui

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
choice = easygui.enterbox(f"Below is the full Monster Card Catalogue:\n\n"
                          f"{cards}\n\n"
                          f"What would you like to delete:", "Delete Card",
                          "enter")

while choice not in catalogue:
    easygui.msgbox(f"Sorry, {choice} is not in the Monster Card Catalogue",
                   "Card Not Found")

    # User enters combo name
    choice = easygui.enterbox(f"Below is the full Monster Card Catalogue:\n\n"
                              f"{cards}\n\n"
                              f"What would you like to delete:",
                              "Delete Card", "enter")

# Remove card from catalogue dictionary
del [catalogue[choice]]
easygui.msgbox(f"{choice} has been deleted from the menu", "Card Removed")
