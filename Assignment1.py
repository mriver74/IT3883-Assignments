# Program Name: Assignment1.py
# Course: IT3883/Section 01
# Student Name: Jack Rivers
# Assignment Number: Lab1
# Due Date: 9/22/26
# Purpose: Program takes user input and adds it to an input buffer. Users can choose from four options, and program mainly runs through a single match statement.
# No specific resources used.

# Set variables
string_to_add = ""
current_string = ""

# Ask user for input
while True:
    option = input("\nPlease choose one of the following options.\nOption 1: Append data to input buffer\nOption 2: Clear input buffer\nOption 3: Display input buffer\nOption 4: Exit program\n")
    match option:
        case "1" | "Option 1" | "option 1":
            # request input, add input to current_string, and clear input
            string_to_add = input("\nEnter string to add to buffer: ")
            current_string = current_string + string_to_add
            print(f"Added '{string_to_add}' to input buffer")
            string_to_add = ""
        case "2" | "Option 2" | "option 2":
            # clear current input buffer
            current_string = ""
            print("\nInput buffer cleared.")
        case "3" | "Option 3" | "option 3":
            # display current input buffer
            print(f"\nCurrent input buffer: '{current_string}'")
        case "4" | "Option 4" | "option 4":
            # exit program via break function
            print("\nExiting program")
            break