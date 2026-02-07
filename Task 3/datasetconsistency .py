n = int(input())
records = []

for _ in range(n):
    records.append(eval(input()))

keys = set(records[0])
print(all(set(r)==keys for r in records))
