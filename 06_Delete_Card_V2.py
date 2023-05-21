"""Component 6 Version 2, Delete Card, Trial 2 using a choice box"""

import easygui

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
cards = []
for card_name, card_info in catalogue.items():
    # Card name added to list
    cards.append(card_name)
text = "Enter any of the following cards to delete:\n"
title = "Delete Card"
delete = easygui.choicebox(text, title, cards)

# Confirm card deletion
sure = easygui.buttonbox(f"Are you sure you want to delete {delete}\n"
                         f"Once it is deleted this cannot be undone",
                         "Delete Confirm", choices=["Yes", "No"])
if sure == "Yes":
    # Remove card from catalogue dictionary
    del [catalogue[delete]]
    easygui.msgbox(f"{delete} has been deleted from the catalogue",
                   "Card Removed")


