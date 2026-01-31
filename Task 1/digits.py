num = int(input("Enter a number: "))
digit = 0
while num > 0:
    digit += 1
    num //= 10
print(f"The number of digits is: {digit}")