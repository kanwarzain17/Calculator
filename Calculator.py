import tkinter as tk

def calculate():

        num1 = int(entry1.get())
        num2 = int(entry2.get())
        opr = operator_var.get()
        if opr == "+":
            result.set (num1 + num2)
        elif opr == "-":
            result.set (num1 - num2)
        elif opr == "*":
            result.set (num1 * num2)
        elif opr == "/":
            if num2 == 0:
                result.set ("Cannot be divided by zero")
            else:
                result.set (num1/num2)
        else:
            result.set ("Invalid syntax")

window = tk.Tk()
window.title("Calculator")

# Entry fields for numbers
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)

entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Label for the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=1, column=0, columnspan=2)

# Dropdown menu for operations
operator_var = tk.StringVar()
operator_choices = ["+", "-", "*", "/"]
operator_var.set(" ")
operator_menu = tk.OptionMenu(window, operator_var, *operator_choices)
operator_menu.grid(row=0, column=2, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=2, padx=10, pady=10)

# Run the GUI
window.mainloop()


