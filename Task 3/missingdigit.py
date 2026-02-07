number = int(input())
digits = [int(d) for d in str(number)]
missing_digit = list(set(range(10)) - set(digits))
print(missing_digit)