n = int(input())
records = []

for _ in range(n):
    records.append(eval(input()))

dup = []
for r in records:
    if records.count(r) > 1 and r not in dup:
        dup.append(r)

print(dup)
