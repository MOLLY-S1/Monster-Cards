""" Component 3 Version 1, Add Card
Trial 2, This code is the same as V1 but uses multiple enter boxes
instead of a multi-enterbox for trialling"""

import easygui

# Card Catalogue
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

# Dictionary for new cards to be added and edited from
new_cards = {}


# User enters power values
card_name = easygui.enterbox("Enter Card Name:", "Card Name")
strength = easygui.integerbox("Enter Strength Value:", "Strength")
speed = easygui.integerbox("Enter Speed Value:", "Speed")
stealth = easygui.integerbox("Enter Stealth Value:", "Stealth")
cunning = easygui.integerbox("Enter Cunning Value:", "Cunning")


# Add the values to the dictionary
new_cards[card_name] = {}
new_cards[card_name]["Strength"] = strength
new_cards[card_name]["Speed"] = speed
new_cards[card_name]["Stealth"] = stealth
new_cards[card_name]["Cunning"] = cunning

# Print full card
card = ""
for card_title, card_info in new_cards.items():
    name = f"\nCard Name: {card_name.title()}"
    for key, value in card_info.items():
        card += f"{key}: {value}\n"

easygui.buttonbox(f"Is the following card correct?\n"
                  f"{name}\n" f"{card}", "Card Check", choices=["Yes", "No"])
