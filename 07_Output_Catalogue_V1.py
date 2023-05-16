"""Component 7 Version 1, Output Catalogue """


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
        # Card name and power values printed
        cards += f"{key}: {value} \n"

print(f"Monster Card Catalogue:\n\n"
      f"{cards}\n\n")
