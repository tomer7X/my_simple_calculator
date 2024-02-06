import tkinter as tk
import math

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    elif button_text == "sqrt":
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("√", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("C", 4, 4),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, command=lambda t=text: on_click(t), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew")

# Adjust row and column weights so that they expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()