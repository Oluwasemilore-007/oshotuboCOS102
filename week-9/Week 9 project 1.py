#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import random

# List of employees and tasks
employees_list = [
    "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
    "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
    "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
]

tasks_list = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]

# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def check_employee(self):
        return self.name in employees_list

    def take_attendance(self):
        return f"Attendance taken for {self.name}."

    def assign_task(self):
        task = random.choice(tasks_list)
        return f"Task assigned to {self.name}: {task}"

    def refuse_access(self):
        return f"Access Denied. {self.name} is not registered as an employee."


# GUI Application
class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Attendance and Task Manager")
        self.root.geometry("450x300")

        self.label = tk.Label(root, text="Enter your full name:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.process_employee, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 11), fg="green")
        self.result_label.pack(pady=10)

    def process_employee(self):
        name = self.entry.get().strip()
        emp = Employee(name)

        if emp.check_employee():
            attendance_msg = emp.take_attendance()
            task_msg = emp.assign_task()
            self.result_label.config(text=f"{attendance_msg}\n{task_msg}", fg="green")
        else:
            deny_msg = emp.refuse_access()
            self.result_label.config(text=deny_msg, fg="red")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()


# In[ ]:




