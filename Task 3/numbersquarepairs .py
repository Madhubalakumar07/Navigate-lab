lst = list(map(int, input().split()))
res = []

for x in lst:
    res.append((x, x*x))

print(res)
