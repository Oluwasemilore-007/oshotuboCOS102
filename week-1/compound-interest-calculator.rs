# Compound Interest Calculator
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest (in %): "))
n = int(input("Enter Number of Times Interest is Applied Per Year: "))
t = float(input("Enter Time (in years): "))

A = P * (1 + (R / n))**(n * t)

print("Total Amount after Compound Interest:", A)
