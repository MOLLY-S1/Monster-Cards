"""Component 4 Version 3, Edit Card, Trial 2 using a message and loop to
edit card"""

import easygui


def edit(confirm_card):
    card = ""
    for card_name, card_info in confirm_card.items():
        title = f"\nCard Name: {card_name}"
        for key, value in card_info.items():
            card += f"{key}: {value}\n"
    correct = easygui.buttonbox(f"Is the following card correct?\n"
                                f"{title}\n" f"{card}", "Card Check",
                                choices=["Yes", "No"])
    if correct == "No":
        easygui.msgbox("Oh no, please re-enter the card information", "Oh No")


# Main Routine
cards = {"Stoneling": {
    "Strength": 7, "Speed": 1,
    "Stealth": 25, "Cunning": 15}}

edit(cards)

