#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

admitted = []
not_admitted = []

def reset_fields():
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    jamb_entry.delete(0, tk.END)
    credits_entry.delete(0, tk.END)
    interview_var.set("Yes")

def submit():
    name = name_entry.get()
    dept = dept_entry.get().strip().lower()
    interview = interview_var.get().strip().lower()

    try:
        jamb_score = int(jamb_entry.get())
        credits = int(credits_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for JAMB score and credits.")
        return

    if dept not in ["computer science", "mass communication"]:
        messagebox.showerror("Error", "Course not valid. Enter 'Computer Science' or 'Mass Communication'.")
        return

    interview_passed = interview == "yes"
    admitted_flag = False

    if dept == "computer science":
        if jamb_score >= 250 and credits >= 5 and interview_passed:
            admitted_flag = True
    elif dept == "mass communication":
        if jamb_score >= 230 and credits >= 5 and interview_passed:
            admitted_flag = True

    if admitted_flag:
        admitted.append(name)
        messagebox.showinfo("Admission Status", f"{name} has met the requirements for {dept.title()} and has been granted admission.")
    else:
        not_admitted.append(name)
        messagebox.showinfo("Admission Status", f"{name} has not met the requirements for {dept.title()}.")

    reset_fields()

def show_results():
    result = "✅ Admitted Candidates:\n" + (", ".join(admitted) if admitted else "None") + "\n\n"
    result += "❌ Not Admitted Candidates:\n" + (", ".join(not_admitted) if not_admitted else "None")
    messagebox.showinfo("Final Results", result)
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Admission Checker")

# Labels & Entries
tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Department:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
dept_entry = tk.Entry(root)
dept_entry.grid(row=1, column=1)

tk.Label(root, text="JAMB Score:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
jamb_entry = tk.Entry(root)
jamb_entry.grid(row=2, column=1)

tk.Label(root, text="Number of Credits:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
credits_entry = tk.Entry(root)
credits_entry.grid(row=3, column=1)

tk.Label(root, text="Passed Interview?").grid(row=4, column=0, padx=10, pady=5, sticky="e")
interview_var = tk.StringVar(value="Yes")
tk.OptionMenu(root, interview_var, "Yes", "No").grid(row=4, column=1)

# Buttons
tk.Button(root, text="Submit Candidate", command=submit, bg="#4CAF50", fg="white").grid(row=5, column=0, pady=15)
tk.Button(root, text="End Input and Show Results", command=show_results, bg="#f44336", fg="white").grid(row=5, column=1)

# Start GUI loop
root.mainloop()

