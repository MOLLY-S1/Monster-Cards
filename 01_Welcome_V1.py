"""Component 1, Version 1, Welcome
This code will create a welcome screen and menu, without using easygui"""

print("Welcome to Monster Card Catalogue\n")

user_choice = input("Please choose an option:\n"
                    "1) Add Card\n"
                    "2) Search Catalogue\n"
                    "3) Delete Card\n"
                    "4) Output Catalogue\n"
                    "5) Exit")

if user_choice == "1":
    print("Add Card")

elif user_choice == "2":
    print("Search Catalogue")

elif user_choice == "3":
    print("Delete Catalogue")

elif user_choice == "4":
    print("Output Catalogue")

elif user_choice == "5":
    print("Exit")
