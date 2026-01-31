n = int(input("enter a number: "))
sum = 0
for i in range(1, 2*n, 2):
    sum += i
print(f"The sum of the first {n} odd numbers is: {sum}")