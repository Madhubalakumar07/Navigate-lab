minutes = int(input("Enter time in minutes: "))
hours = minutes //60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")