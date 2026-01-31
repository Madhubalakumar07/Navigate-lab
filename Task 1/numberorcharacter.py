question = input("Enter a number or character: ").strip().lower()
if question.isdigit():
    print(f"{question} is a number.")
elif question.isalpha():
    print(f"{question} is a character.")
else:
    print("it is a special character.")
