number = int(input("Enter a number: "))
odd_digit = 0
even_digit = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        even_digit += 1
    else:
        odd_digit += 1
    number //= 10
print(f"The number of even digits is: {even_digit}")
print(f"The number of odd digits is: {odd_digit}")