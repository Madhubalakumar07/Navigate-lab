lst = list(map(int, input().split()))
k = int(input())
d = {}

for x in lst:
    d[x] = d.get(x,0) + 1

print(sorted(d, key=d.get, reverse=True)[:k])
