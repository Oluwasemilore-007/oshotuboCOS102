# Annuity Plan Calculator
PMT = float(input("Enter Payment Amount (PMT): "))
R = float(input("Enter Rate of Interest (in %): "))
n = int(input("Enter Number of Times Interest Applied Per Year: "))
t = float(input("Enter Time (in years): "))

# Convert R to a fraction
R = R / 100

# Calculate annuity amount
A = PMT * ((1 + (R / n))**(n * t) - 1) / (R / n)

print("Total Amount for Annuity Plan:", A)
