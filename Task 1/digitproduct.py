number = int(input("enter a number: "))
product = 1
while number > 0:
    digit = number % 10
    product *= digit
    number //= 10
print(f"The product of the digits is: {product}")