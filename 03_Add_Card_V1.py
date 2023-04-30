"""Component 3 Version 1, Add Card
Trial 1, this code asks questions using a multi-enterbox"""

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


# Dictionary for new card to be added and edited from
new_cards = {}


# User enters title values
text = "Enter the value of the listed power"
title = "Card Enter"
input_list = ["Card Name", "Strength", "Speed", "Stealth", "Cunning"]
values = easygui.multenterbox(text, title, input_list)


# Add the user combo and prices to the dictionary
new_cards[values[0]] = {}
new_cards[values[0]][input_list[1]] = values[1]
new_cards[values[0]][input_list[2]] = values[2]
new_cards[values[0]][input_list[3]] = values[3]

card = ""
for card_name, card_info in new_cards.items():
    card_name = f"\nCard Name: {card_name}"
    for key, value in card_info.items():
        card += f"{key}: {value}\n"


easygui.buttonbox(f"Is the following card correct?\n"
                  f"{card_name}\n" f"{card}", "Card Check", choices=["Yes", "No"])
