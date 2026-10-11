# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Jack Rivers
# Assignment Number: Lab#3
# Due Date: 10/10/2026
# Purpose: The program opens up a GUI that converts gallon per mile to liter per kilometer. The program
# takes an input, multiplies it by a variable, and constantly updates it to show onscreen. If the entered
# number is invalid, a message displays describing what the user needs to do.
# "tkinter" library was used for this assignment.

# import tkinter library
import tkinter as tk

# define functions
def convert(*args):
    try:
        mpg = float(mpg_amount.get())
        if mpg < 0:
            result.set("Enter a positive number.")
        else:
            kilo_per_liter = mpg * 0.425143707
            result.set(f"{kilo_per_liter:.2f} km/L")
    except ValueError:
        result.set("Enter a valid number.")

# create main popup
main = tk.Tk()
main.title("MPG to KM/L Calc")
main.geometry("400x160")
main.resizable(False, False)

# create input/output var
mpg_amount = tk.StringVar()
result = tk.StringVar(value="Enter a number.")

# create title for popup
title_label = tk.Label(main, text="Miles per Gallon -> Kilometers per Liter")
title_label.pack(pady=5)

# create input label for popup
input_label = tk.Label(main, text="Miles per Gallon (mpg):")
input_label.pack()

# create input for popup
mpg_entry = tk.Entry(main, textvariable=mpg_amount)
mpg_entry.pack(pady=5)

# convert when input changes
mpg_amount.trace_add("write", convert)

# create output for popup
output_label = tk.Label(main, text="Kilometers per Liter (km/L):")
output_label.pack(pady=5)

# display results
result_label = tk.Label(main, textvariable=result)
result_label.pack()

# initialize gui
main.mainloop()
