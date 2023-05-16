""" Component 3 Version 3, Add Card
Builds on my chosen trialled code of V2, now uses the blank and boundaries
are now added to the integer boxes"""

import easygui


# Blank checker function
def blank_check(question, title, box):
    error = "Please answer all questions"
    while True:
        # Enter-box
        if box == "enter":
            # Ask for input
            response = easygui.enterbox(question, title)

            # If cancel is pressed
            if not response:
                easygui.msgbox(error, "Error")

            # If valid response
            else:
                return response

        else:
            # Ask for input
            response = easygui.integerbox(question, title, upperbound=25,
                                          lowerbound=0)

            # If cancel is pressed
            if not response:
                easygui.msgbox(error, "Error")

            # If valid response
            else:
                return response


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
card_name = blank_check("Enter Card Name:", "Card Name", "enter")
strength = blank_check("Enter Strength Value:", "Strength",
                       "integer")
speed = blank_check("Enter Speed Value:", "Speed", "integer")
stealth = blank_check("Enter Stealth Value:", "Stealth", "integer")
cunning = blank_check("Enter Cunning Value:", "Cunning", "integer")

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
