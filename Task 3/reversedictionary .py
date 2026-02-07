n = int(input())
d = {}

for _ in range(n):
    k = input()
    v = input()
    d[k] = v

rev = {v:k for k,v in d.items()}
print(rev)
