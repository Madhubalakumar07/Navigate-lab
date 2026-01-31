number = int(input("Enter a number: "))
num = number
digit = 0
while number > 0:
    digit += 1
    number //= 10
number = num
amstrong = 0
for i in range(digit):
    amstrong += (num % 10) ** digit
    num //= 10
if amstrong == number:  
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")