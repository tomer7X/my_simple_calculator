import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import cmath

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
    elif button_text == "√":
        try:
            result = math.sqrt(float(current_text))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif button_text == "mod53":
        open_mod53_window()
    else:
        entry_var.set(current_text + button_text)

def open_mod53_window():
    mod53_window = tk.Toplevel(root)
    mod53_window.title("Mod53 Calculator")

    a_label = tk.Label(mod53_window, text="Enter value for a:")
    a_label.pack()

    a_entry = tk.Entry(mod53_window)
    a_entry.pack()

    b_label = tk.Label(mod53_window, text="Enter value for b:")
    b_label.pack()

    b_entry = tk.Entry(mod53_window)
    b_entry.pack()

    c_label = tk.Label(mod53_window, text="Enter value for c:")
    c_label.pack()

    c_entry = tk.Entry(mod53_window)
    c_entry.pack()

    calculate_button = tk.Button(mod53_window, text="Calculate", command=lambda: calculate_mod53(a_entry.get(), b_entry.get(), c_entry.get()))
    calculate_button.pack()

def calculate_mod53(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        discriminant = b**2 - 4*a*c
        sqrt_discriminant = cmath.sqrt(discriminant)

        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)

        if x1 == x2:
            result_text = f"x = {x1}"
        elif x1.imag == 0:
            result_text = f"x1 = {x1.real}, x2 = {x2.real}"
        else:
            result_text = f"x1 = {x1}, x2 = {x2}"

        messagebox.showinfo("Mod53 Result", result_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values for a, b, and c.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("√", 5, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 5, 0),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 5, 1),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("C", 5, 3,),
    ("mod53", 3, 5)  # Button for mod53 calculation
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
