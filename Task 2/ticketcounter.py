ticket_price = 200
age = int(input("Enter your age: "))
if age <= 5:
    ticket_price = 0
elif age <= 12:
    ticket_price *= 0.5
elif age >= 60:
    ticket_price *= 0.7
print(f"Your ticket price is: ${ticket_price:.2f}")