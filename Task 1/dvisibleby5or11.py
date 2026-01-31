number = int(input("Enter a number: "))
if number % 5 == 0 or number % 11 == 0:
    print(f"{number} is divisible.")
else:
    print(f"{number} is not divisible.")