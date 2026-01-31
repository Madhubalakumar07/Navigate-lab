character = input("Enter a character: ").lower()
vowels = 'aeiou'
if character in vowels:
    print(f"{character} is a vowel.")
else:
    print(f"{character} is not a vowel.")