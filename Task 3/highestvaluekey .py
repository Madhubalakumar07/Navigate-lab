n = int(input())
d = {}

for _ in range(n):
    k = input()
    v = int(input())
    d[k] = v

print(max(d, key=d.get))
