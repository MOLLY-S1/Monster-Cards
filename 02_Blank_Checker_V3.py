""" Component 2 Version 3,  Blank Checker
Code has been built on from V2, now a function
"""
import easygui


# Blank checker function
def blank_check(question, title):
    error = "Please answer all questions"
    while True:
        # Ask for input
        response = easygui.enterbox(question, title)

        # If cancel is pressed
        if not response:
            easygui.msgbox(error, "Error")

        # If valid response
        else:
            return response


# Main Routine
enter = blank_check("Enter:", "Enter")
