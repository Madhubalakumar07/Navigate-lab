n = int(input())
data = []

for _ in range(n):
    data.append(eval(input()))

summary = {"rows": n, "unique_values": {}}

for k in data[0]:
    summary["unique_values"][k] = len({d[k] for d in data})

print(summary)
