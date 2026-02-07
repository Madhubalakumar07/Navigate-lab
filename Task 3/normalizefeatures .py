d = eval(input())
total = sum(d.values())

for k in d:
    d[k] = d[k]/total

print(d)
