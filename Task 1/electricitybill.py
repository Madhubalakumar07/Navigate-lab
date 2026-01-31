units = int(input("Enter the number of units consumed: "))
bill = 0
if units < 0:
    print("Invalid input. Units cannot be negative.")
elif units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7    
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print(f"The electricity bill for {units} units is: Rs. {bill}")