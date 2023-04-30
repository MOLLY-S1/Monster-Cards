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


# User enters item names
card_name = easygui.enterbox("Enter Card Name:", "Card Name")
strength = easygui.enterbox("Enter Strength Value:", "Value")
Speed = easygui.enterbox("Enter Speed Value:", "Speed")
Stealth = easygui.enterbox("Enter Stealth Value:", "Stealth")
drink = easygui.enterbox("Enter Cunning Value:", "Cunning")

# User enters item prices
burger_price = easygui.enterbox(f"Enter {burger} Price", "Burger Price")
side_price = easygui.enterbox(f"Enter {side} Price", "Side Price")
drink_price = easygui.enterbox(f"Enter {drink} Price", "Drink Price")

# Add the user combo and prices to the dictionary
new_combos[combo_name] = {}
new_combos[combo_name][burger] = burger_price
new_combos[combo_name][side] = side_price
new_combos[combo_name][drink] = drink_price

combo = ""
for combo_ID, combo_info in new_combos.items():
    ID = f"\nCombo Name: {combo_ID.title()}"
    for key, value in combo_info.items():
        combo += f"{key}: {value}\n"

easygui.buttonbox(f"Is the following combo correct?\n"
                  f"{ID}\n" f"{combo}", "Combo Check", choices=["Yes", "No"])
