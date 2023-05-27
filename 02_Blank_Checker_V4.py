"""Component 2 Version 4,  Blank Checker,
Code has been built on from V3, now includes an integer-box blank checker
within the function"""

import easygui


# Blank checker function
def blank_check(question, title, box):
    error = "Please answer all questions"
    while True:
        # Enter-box
        if box == "enter":
            # Ask for input
            response = easygui.enterbox(question, title)

            if response == "":
                easygui.msgbox(error, "Error")

            # If cancel is pressed
            if not response:
                print("Return to menu")

            # If valid response
            else:
                return response

        elif box == "integer":
            # Ask for input
            response = easygui.integerbox(question, title, lowerbound=1,
                                          upperbound=25)

            # If cancel is pressed
            if not response:
                print("Return to menu")

            # If valid response
            else:
                return response


# Main Routine
blank_check("enter:", "enter", "integer")
blank_check("enter:", "enter", "enter")
