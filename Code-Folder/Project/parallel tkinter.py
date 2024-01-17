import tkinter as tk
from tkinter import messagebox

def calculate_parallel_resistance():
    try:
        resistors = [float(resistor.get()) for resistor in resistor_entries]
        total_resistance = 1 / sum(1 / r for r in resistors if r != 0)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return
    except ZeroDivisionError:
        messagebox.showerror("Error", "Resistance cannot be zero")
        return

    result_label.config(text=f"Total Resistance: {total_resistance:.2f} Ohms")

root = tk.Tk()
root.title("Parallel Resistance Calculator")

resistor_entries = []
for i in range(5):  # assuming maximum 5 resistors
    tk.Label(root, text=f"Resistor {i+1} (Ohms):").grid(row=i, column=0, sticky='e')
    resistor = tk.Entry(root)
    resistor.grid(row=i, column=1)
    resistor_entries.append(resistor)

calculate_button = tk.Button(root, text="Calculate", command=calculate_parallel_resistance)
calculate_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()