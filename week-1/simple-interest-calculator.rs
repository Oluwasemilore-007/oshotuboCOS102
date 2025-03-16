# Simple Interest Calculator
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest (in %): "))
T = float(input("Enter Time (in years): "))

A = P * (1 + (R / 100) * T)

print("Total Amount after Simple Interest:", A)
