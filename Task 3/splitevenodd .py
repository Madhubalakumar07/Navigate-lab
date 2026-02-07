lst = list(map(int, input().split()))
even = []
odd = []

for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(even, odd)
