"""
Beginner-Friendly Calculator using Tkinter

How to run:
1. Save this file as calculator_tkinter.py
2. Open terminal / command prompt in the same folder
3. Run: python calculator_tkinter.py
"""

import tkinter as tk


# This function is called when a number or operator button is clicked
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)


# This function clears everything from the display
def clear_display():
    entry.delete(0, tk.END)


# This function deletes the last character from the display
def delete_last():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])


# This function calculates the final answer
def calculate_answer():
    try:
        expression = entry.get()

        # Replace symbols with Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        answer = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, str(answer))

    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by zero")

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid input")


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("415x465")
window.resizable(False, False)
window.configure(bg="#f2f2f2")

# Create the display entry box
entry = tk.Entry(
    window,
    font=("Arial", 24),
    borderwidth=2,
    relief="solid",
    justify="right"
)
entry.pack(padx=10, pady=20, fill="x")

# Create a frame to hold all buttons
button_frame = tk.Frame(window, bg="#f2f2f2")
button_frame.pack()

# Button layout
buttons = [
    ["C", "DEL", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."]
]


# Function to create buttons easily
def create_button(text, row, column, columnspan=1):
    if text == "C":
        command = clear_display
        bg_color = "#ff9999"
    elif text == "DEL":
        command = delete_last
        bg_color = "#ffcc99"
    elif text == "=":
        command = calculate_answer
        bg_color = "#99ccff"
    else:
        command = lambda: button_click(text)
        bg_color = "#ffffff"

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        width=6,
        height=2,
        bg=bg_color,
        command=command
    )
    button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)


# Add buttons to the window
for row_index, row in enumerate(buttons):
    for column_index, button_text in enumerate(row):
        if button_text == "0":
            create_button(button_text, row_index, column_index, columnspan=2)
        elif button_text == ".":
            create_button(button_text, row_index, column_index + 1)
        else:
            create_button(button_text, row_index, column_index)

# Start the Tkinter event loop
window.mainloop()