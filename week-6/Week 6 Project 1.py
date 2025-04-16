#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        weight = float(weight_entry.get())
        location = location_var.get()

        if location == "Ibeju-Lekki":
            if weight >= 10:
                cost = 5000
            else:
                cost = 3500
        elif location == "Epe":
            if weight >= 10:
                cost = 10000
            else:
                cost = 5000
        else:
            messagebox.showerror("Error", "Please select a valid location.")
            return

        result_label.config(text=f"Delivery Cost: ₦{cost}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid weight.")

# GUI setup
root = tk.Tk()
root.title("Simi Services Delivery Calculator")
root.geometry("400x300")

# 🔥 Welcome Message
tk.Label(root, text="Welcome to Simi Services!", font=("Helvetica", 16, "bold"), fg="green").pack(pady=10)

# Location input
tk.Label(root, text="Select Location:").pack(pady=5)
location_var = tk.StringVar(value="Ibeju-Lekki")
tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe").pack()

# Weight input
tk.Label(root, text="Enter Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Calculate button
tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

root.mainloop()


# In[ ]:




