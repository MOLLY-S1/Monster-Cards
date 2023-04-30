"""Component 2 Version 1, Blank Checker
This Component ensures all boxes are answered"""
import easygui

# User input
enter = easygui.enterbox("Enter here:", "Enter")

# Continue looping until valid is entered
while enter == "":
    easygui.msgbox("Please answer all questions", "Error")
    enter = easygui.enterbox("Enter here:", "Enter")
