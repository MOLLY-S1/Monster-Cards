""" Component 2 Version 3,  Blank Checker
Code has been built on from V2, now a function
"""
import easygui


# Blank checker function
def blank_check(question):
    error = "That was not a valid input\n" \
            "Please answer all questions"

    while True:
        try:
            # Ask for input
            response = easygui.enterbox(question, "ENTER")

            # Check if answer is given
            if response != "":
                return response

            else:
                easygui.msgbox(error, "ERROR")

        # Allow all values
        except ValueError:
            easygui.msgbox(error, "ERROR")


# Main Routine
enter = blank_check("Enter:")
