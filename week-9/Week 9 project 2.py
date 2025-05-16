#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox


class DeliveryService:
    def __init__(self, location, weight):
        self.location = location
        self.weight = weight

    def calculate_cost(self):
        try:
            weight = float(self.weight)
            if self.location == "PAU":
                return 2000 if weight >= 10 else 1500
            elif self.location == "Epe":
                return 5000 if weight >= 10 else 4000
            else:
                return None
        except ValueError:
            return None


# GUI Application
class DeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delivery Cost Calculator")
        self.root.geometry("400x300")

        # Location label and dropdown
        self.location_label = tk.Label(root, text="Select Location:", font=("Arial", 12))
        self.location_label.pack(pady=10)

        self.location_var = tk.StringVar(value="Select Location")  # default value
        self.location_dropdown = tk.OptionMenu(root, self.location_var, "PAU", "Epe")
        self.location_dropdown.config(width=20)
        self.location_dropdown.pack()

        # Weight label and entry
        self.weight_label = tk.Label(root, text="Enter Package Weight (kg):", font=("Arial", 12))
        self.weight_label.pack(pady=10)

        self.weight_entry = tk.Entry(root, font=("Arial", 12))
        self.weight_entry.pack()

        # Submit button
        self.submit_button = tk.Button(root, text="Calculate Cost", command=self.calculate_cost, font=("Arial", 12))
        self.submit_button.pack(pady=20)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()

    def calculate_cost(self):
        location = self.location_var.get()
        weight = self.weight_entry.get().strip()

        if location not in ["PAU", "Epe"]:
            messagebox.showerror("Input Error", "Please select a valid delivery location.")
            return

        if not weight:
            messagebox.showerror("Input Error", "Please enter the package weight.")
            return

        service = DeliveryService(location, weight)
        cost = service.calculate_cost()

        if cost is None:
            self.result_label.config(text="Invalid weight input. Please enter a number.", fg="red")
        else:
            self.result_label.config(text=f"Delivery Cost: ₦{cost}", fg="green")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = DeliveryApp(root)
    root.mainloop()


# In[ ]:




