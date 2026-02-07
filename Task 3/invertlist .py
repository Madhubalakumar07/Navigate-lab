n = int(input())
d = {}

for _ in range(n):
    s = input()
    dept = input()
    d[s] = dept

res = {}
for k,v in d.items():
    res.setdefault(v, []).append(k)

print(res)
