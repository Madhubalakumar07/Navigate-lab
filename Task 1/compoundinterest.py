principle = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))
coumpound_interest = principle * (1 + rate / 100) ** time - principle
print("The Compound Interest is:", coumpound_interest)