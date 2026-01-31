a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a+b
d = a**b
if c > d:
    print(f"The sum {c} is greater than the power {d}.")
elif d > c:
    print(f"The power {d} is greater than the sum {c}.")
else:
    print(f"The sum {c} and power {d} are equal.")