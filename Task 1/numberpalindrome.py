number = int(input("Enter a number: "))
num = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if num == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")