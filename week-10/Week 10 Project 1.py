#!/usr/bin/env python
# coding: utf-8

# In[14]:


import tkinter as tk
from tkinter import messagebox


# Parent class
class Zenith:
    def __init__(self, name):
        self.name = name

    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]

    def unique_services(self):
        return []


# Child class for Retail Banking
class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ]


# Child class for Global Banking
class GlobalBanking(Zenith):
    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]


# Child class for Commercial Banking
class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Advisory services"
        ]


# GUI class
class ZenithApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zenith Bank Division Services")
        self.root.geometry("500x400")

        # Name input
        tk.Label(root, text="Enter Employee Name:", font=("Arial", 12)).pack(pady=10)
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.pack()

        # Division input
        tk.Label(root, text="Select Division:", font=("Arial", 12)).pack(pady=10)
        self.division_var = tk.StringVar()
        self.division_var.set("Select Division")
        tk.OptionMenu(root, self.division_var, "Retail", "Global", "Commercial").pack()

        # Submit button
        tk.Button(root, text="Show Services", command=self.show_services, font=("Arial", 12)).pack(pady=20)

        # Result display
        self.result_text = tk.Text(root, height=12, width=60, font=("Arial", 10))
        self.result_text.pack()

    def show_services(self):
        name = self.name_entry.get().strip()
        division = self.division_var.get()

        if not name or division == "Select Division":
            messagebox.showerror("Input Error", "Please enter name and select a division.")
            return

        # Instantiate correct class based on division
        if division == "Retail":
            employee = RetailBanking(name)
        elif division == "Global":
            employee = GlobalBanking(name)
        elif division == "Commercial":
            employee = CommercialBanking(name)
        else:
            messagebox.showerror("Error", "Unknown division selected.")
            return

        # Compose result text
        services = employee.mutual_services() + employee.unique_services()
        result = f"Employee Name: {employee.name}\nDivision: {division} Banking\n\nServices:\n"
        result += "\n".join(f"- {service}" for service in services)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ZenithApp(root)
    root.mainloop()


# In[ ]:




