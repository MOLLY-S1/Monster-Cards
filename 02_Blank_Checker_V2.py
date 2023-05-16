""" Component Version 2, Blank Checker
built on from version 1, now in a loop and allows cancel buttons"""
import easygui

error = "Please answer all questions\n"
valid = False

# Continue asking until a valid amount is entered
while not valid:
    # Ask for input
    response = easygui.enterbox("Enter: ")

    # If cancel is pressed
    if not response:
        easygui.msgbox(error, "Error")

    # If valid response
    else:
        break


