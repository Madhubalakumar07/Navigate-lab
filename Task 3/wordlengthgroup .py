words = input().split()
d = {}

for w in words:
    d.setdefault(len(w), []).append(w)

print(d)
