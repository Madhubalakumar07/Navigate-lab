days = int(input("Enter the number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
remaining_days %= 7
print(f"{days} days is equal to {years} years, {weeks} weeks and {remaining_days} days.")