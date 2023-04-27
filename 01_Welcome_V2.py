"""Component 1, Version 2, Welcome Screen
Trial 2, This code will create a welcome screen and menu, using easygui"""
import easygui

# Welcome message
easygui.msgbox("Welcome to Monster Card Catalogue", "Welcome")

# User enters choice
user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                choices=["Add Cards", "Search Catalogue",
                                         "Delete Card", "Output Catalogue",
                                         "Exit"])
# Output user choice
if user_choice == "Add Card":
    easygui.msgbox("Add Card", "Add Card")

elif user_choice == "Search Catalogue":
    easygui.msgbox("Search Catalogue", "Search Catalogue")

elif user_choice == "Delete Card":
    easygui.msgbox("Delete Card", "Delete Card")

elif user_choice == "Output Catalogue":
    easygui.msgbox("Output Catalogue", "Output Catalogue")

elif user_choice == "Exit":
    easygui.msgbox("Goodbye", "Exit")
