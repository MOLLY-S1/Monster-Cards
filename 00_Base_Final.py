"""Base Component
Final version of code after testing, trialling and end-user testing
"""

import easygui


# Function to display menu and welcome screen
def welcome():
    # Enter user choice
    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Cards", "Search Catalogue",
                                             "Delete Card", "Output Catalogue",
                                             "Exit"])

    # Call on corresponding functions
    while user_choice != "Exit":
        if user_choice == "Add Cards":
            add_card(catalogue)

        elif user_choice == "Search Catalogue":
            search_card(catalogue)

        elif user_choice == "Delete Card":
            delete_card(catalogue)

        elif user_choice == "Output Catalogue":
            output_catalogue(catalogue)

    easygui.msgbox("Goodbye", "Goodbye")
    exit()


# Blank checker function
def blank_check(question, title, box):
    # Error statement
    error = "Please answer all questions"
    while True:
        # Enter-box
        if box == "enter":
            # Ask for input
            response = easygui.enterbox(question, title)

            # If nothing is entered
            if response == "":
                easygui.msgbox(error, "Error")

            # If cancel is pressed
            if not response:
                welcome()

            # If valid response
            else:
                return response

        elif box == "integer":
            # Ask for input
            response = easygui.integerbox(question, title, lowerbound=1,
                                          upperbound=25)

            # If cancel is pressed
            if not response:
                welcome()

            # If valid response
            else:
                return response


# Function to confirm and edit cards
def edit(confirm_card, card_list):
    while True:
        card = ""
        powers = ""
        card_name = ""
        title = ""
        # Print card information
        for card_name, card_info in confirm_card.items():
            title = f"\nCard Name: {card_name}"
            for key, value in card_info.items():
                card += f"{key}: {value}\n"
                powers += f"-{key}-"

        # Check if correct
        correct = easygui.buttonbox(f"Is the following card correct?\n"
                                    f"{title}\n" f"{card}", "Card Check",
                                    choices=["Yes", "No"])

        # If correct add card to catalogue
        if correct == "Yes":
            easygui.msgbox(f"You have successfully entered the new card "
                           f"{card_name} to the Monster Cards Catalogue",
                           "Card added")
            return confirm_card

        # Edit card info
        change_value = easygui.buttonbox("What would you like to change?",
                                         "Change Choice",
                                         choices=["Power Value",
                                                  "Card Name", ])

        # Edit power value
        if change_value == "Power Value":
            current_value = blank_check("Enter the name of the power "
                                        "which value you wish to "
                                        "change:", "Power Name",
                                        "enter").title()

            # If invalid power is entered
            while current_value not in confirm_card[card_name]:
                easygui.msgbox("Sorry, that is not the name of "
                               "a power in this card:\n\n"
                               f"{title}\n" f"{card}", "Error")

                current_value = blank_check(f"Enter the name of the "
                                            "power which value you wish "
                                            "to change:\n"
                                            f"The options are: {powers} ",
                                            "Power Name", "enter").title()

            # Enter new value
            new = blank_check(f"Enter the value you want to change"
                              f" {current_value} to:", "New Value",
                              "integer")

            # Update Card
            confirm_card[card_name][current_value] = new

        # Edit card name
        elif change_value == "Card Name":
            new = blank_check(f"Enter the name you want to change "
                              f"{card_name} to:", "New Name", "enter").title()

            # Ensure it is a unique name
            if new in card_list:
                new = blank_check(f"Sorry that name already is already taken!"
                                  f" Enter the name you want to change "
                                  f"{card_name} to:", "New Name",
                                  "enter").title()

            # Update Card info
            confirm_card[new] = confirm_card.pop(card_name)


# Function to add a new card
def add_card(card_list):
    # Dictionary for new cards to be added and edited from
    new_cards = {}

    # User enters power values
    name = blank_check("Enter Card Name:", "Card Name", "enter").title()
    checked_name = name.title()

    # Check if the entered name is already in the catalogue
    while checked_name in card_list:
        easygui.msgbox(f"Sorry a card with the name {name} already exists in "
                       f"this catalogue, please choose another name",
                       "Error")
        name = blank_check("Enter Card Name:", "Card Name", "enter"). \
            title()

    # Enter the value of each power
    strength = blank_check("Enter Strength Value:", "Strength",
                           "integer")
    speed = blank_check("Enter Speed Value:", "Speed", "integer")
    stealth = blank_check("Enter Stealth Value:", "Stealth", "integer")
    cunning = blank_check("Enter Cunning Value:", "Cunning", "integer")

    # Add the values to the dictionary
    new_cards[name] = {}
    new_cards[name]["Strength"] = strength
    new_cards[name]["Speed"] = speed
    new_cards[name]["Stealth"] = stealth
    new_cards[name]["Cunning"] = cunning

    # Confirm card is correct
    correct_card = edit(new_cards, card_list)

    # Update correct card to card list and return to menu
    card_list.update(correct_card)
    welcome()


# Function to search catalogue for card
def search_card(card_list):
    while True:
        # User enters card name
        search_name = blank_check("Enter name of card: ", "Search",
                                  "enter").title()

        # If the name searched doesn't exist
        while search_name not in card_list:
            easygui.msgbox(
                f"Sorry {search_name} is not a card in the Monster Card "
                f"catalogue", "Card Not Found")

            # Ask user to continue searching
            back = easygui.buttonbox("Would you like to continue searching?",
                                     "Continue?", choices=["Yes", "No"])

            # If no return to menu
            if back == "No":
                welcome()

            # User enters card name
            search_name = blank_check("Enter name of card: ", "Search",
                                      "enter").title()

        # Add the searched card to separate dictionary
        searched_card = {search_name: card_list[search_name]}

        # Confirm the searched card
        correct_card = edit(searched_card, card_list)

        # Update the catalogue and return to menu
        del [card_list[search_name]]
        card_list.update(correct_card)
        welcome()


# Function to delete cards from catalogue
def delete_card(card_list):
    # List of card names
    cards = []
    for card_name, card_info in card_list.items():
        # Card name added to list
        cards.append(card_name)

    # Information to create choice-box
    text = "Enter any of the following cards to delete:\n"
    title = "Delete Card"
    delete = easygui.choicebox(text, title, cards)

    # If cancel is pressed
    if not delete:
        welcome()

    # Confirm card deletion
    sure = easygui.buttonbox(f"Are you sure you want to delete {delete}\n"
                             f"Once it is deleted this cannot be undone",
                             "Delete Confirm", choices=["Yes", "No"])

    # If confirmed remove card and return to menu
    if sure == "Yes":
        # Remove card from catalogue dictionary
        del [card_list[delete]]
        easygui.msgbox(f"{delete} has been deleted from the catalogue",
                       "Card Removed")
        welcome()

    # Return to menu
    welcome()


# Function to print full catalogue
def output_catalogue(card_list):
    cards = ""

    # loop to print dictionary
    for card_name, card_info in card_list.items():

        # Card name printed
        cards += f"\n{card_name}\n" \
                 f"------------------\n"

        # Loop to print dictionary inside the dictionary
        for key, value in card_info.items():
            # Card name and power values printed
            cards += f"{key}: {value} \n"

    # Formatted output
    full_output = f"-----------------------\n" \
                  f"Monster Card Catalogue:\n" \
                  f"-----------------------\n" \
                  f"{cards}\n\n"

    # Print full list to python console and return to menu
    print(full_output)
    welcome()


# MAIN ROUTINE

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

# Welcome message
easygui.msgbox("------------------------------------------------------------\n"
               "Welcome to the Monster Card Catalogue\n"
               "-------------------------------------------------------------",
               "Welcome")
# Begin program
welcome()
