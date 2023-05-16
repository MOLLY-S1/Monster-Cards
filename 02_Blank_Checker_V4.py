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


# Main Routine
blank_check("enter:", "enter", "integer")
blank_check("enter:", "enter", "enter")
