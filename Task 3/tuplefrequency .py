n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

d = {}
for t in lst:
    d[t] = d.get(t, 0) + 1

print(d)
