number = int(input("Enter a number: "))
i = 2
isprime =True
while i < number:
    if number % i == 0:
        isprime = False
        break
    i += 1
if isprime and number > 1:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")