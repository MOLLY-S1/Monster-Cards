"""Component 2 Version 4,  Blank Checker,
Code has been built on from V3, now includes an integer-box blank checker
within the function and allows for the cancel button to be pressed"""

import easygui


# Blank checker function
def blank_check(question, title, box):
    error = "That was not a valid input\n" \
            "Please answer all questions"

    while True:
        # Enter-box
        if box == "enter":
            try:
                # Ask for input
                response = easygui.enterbox(question, title)

                # If cancel is pressed
                if not response:
                    easygui.msgbox(error, "ERROR")

                # Check if answer is given
                if response != "":
                    return response

                # Show error
                else:
                    easygui.msgbox(error, "ERROR")

            # Allow all values
            except ValueError:
                easygui.msgbox(error, "ERROR")

        # Integer-box
        elif box == "integer":
            try:
                # Ask for input
                response = easygui.integerbox(question, title,
                                              upperbound=25, lowerbound=0)

                # If cancel is pressed
                if not response:
                    easygui.msgbox(f"{error}, all integers must be between "
                                   f"1 and 25", "Error")

                # Check if answer is given
                if response != "":
                    return response

                # Show error message
                else:
                    easygui.msgbox(f"{error}, all integers must be between "
                                   f"1 and 25", "Error")

            # Allow all values
            except ValueError:
                easygui.msgbox(f"{error}, all integers must be between "
                                   f"1 and 25", "Error")


# Main Routine
blank_check("enter:", "enter", "integer")
blank_check("enter:", "enter", "enter")
