a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print(f"The roots are real and different: {root1} and {root2}") 
elif d == 0:
    root = -b / (2*a)
    print(f"The roots are real and the same: {root}")
else:
    print("The roots are complex and different.")