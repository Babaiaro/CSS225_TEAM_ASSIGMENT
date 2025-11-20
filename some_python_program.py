# Program description goes here
# Simple GUI calculator program using the tkinter library for basic arithmetic.
# Updated on: 2025-11-20
# Updated by: Babaiar Kenzhebekov
#
#
# Document what the following lines of code do here
from tkinter import *
# Imports all classes and functions from the tkinter GUI library.

root = Tk()
# Initializes the main window/container widget.

root.title("Simple Calculator")
# Sets the title of the application window.

# Document what the following lines of code do here
e = Entry(root, width=35, borderwidth=5)
# Creates the Entry widget (the calculator display) in the root window.
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Places the display at the top (row 0), spanning three columns, with padding.

# Document what the following lines of code do here
def button_click(number):
    # Function called when a number button (0-9) is pressed.
    current = e.get()
    # Retrieves the current content of the display.
    e.delete(0, END)
    # Clears the display entirely.
    e.insert(0, str(current) + str(number))
    # Concatenates the old content with the new digit and inserts the result.

# Document what the following lines of code do here
def button_clear():
    # Function called by the 'Clear' button.
    e.delete(0, END)
    # Deletes all text from the display, resetting the input.

# Document what the following lines of code do here
def button_operator(operator):
    # Function called when an arithmetic operator (+, -, *, /) is pressed.
    first_number = e.get()
    # Captures the number currently displayed (the first operand).
    global f_num
    # Declares f_num as a global variable.
    global num_operator
    # Declares num_operator as a global variable.
    f_num = int(first_number)
    # Converts the first operand to an integer and assigns it to f_num.
    num_operator = operator
    # Stores the specific operator symbol (e.g., '+').
    e.delete(0, END)
    # Clears the display to allow input of the second operand.

# Document what the following lines of code do here

# Function to perform the final calculation when the '=' button is pressed.
def button_equal():
    second_number = e.get()
    # Retrieves the second operand from the display.
    e.delete(0, END)
    # Clears the display for the result.
    if num_operator == '+':
        # Checks the stored operator and performs addition.
        e.insert(0, f_num + int(second_number))
    elif num_operator == '*':
        # Performs multiplication.
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        # Performs division.
        e.insert(0, f_num / int(second_number))
    elif num_operator == '-':
        # Performs subtraction.
        e.insert(0, f_num - int(second_number))
    else:
        # Handles any unexpected operator value.
        e.insert(0, "Invalid!!!")

# Document what the following lines of code do here
#
# NOTE: A Lambda function is a small anonymous function used here to pass an argument
# to a command function when a button is clicked.

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# Defines the '1' button. Uses lambda to call button_click with argument 1.
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
# Defines the '+' button. Uses lambda to call button_operator with argument '+'.
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
# Defines the '=' button. Calls button_equal directly.
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# Defines the 'Clear' button. Calls button_clear directly.

# Document what the following lines of code do here

# Button definitions for remaining operators.
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
# Defines the '-' button.
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
# Defines the '*' (multiply) button.
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))
# Defines the '/' (divide) button.

# Document what the following lines of code do here

button_1.grid(row=3, column=0)
# Places button '1' in the grid.
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
# Places button '0'.
button_add.grid(row=5, column=0)
# Places the '+' button.
button_equal.grid(row=5, column=1, columnspan=2)
# Places the '=' button, spanning two columns.
button_clear.grid(row=4, column=1, columnspan=2)
# Places the 'Clear' button, spanning two columns.

button_subtract.grid(row=6, column=0)
# Places the '-' button.
button_multiply.grid(row=6, column=1)
# Places the '*' button.
button_divide.grid(row=6, column=2)
# Places the '/' button.

# Document what the following line of code do here

root.mainloop()
# Starts the Tkinter event loop, keeping the GUI window open and responsive.