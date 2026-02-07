n = int(input())
d1 = {}
d2 = {}

for _ in range(n):
    k = input()
    d1[k] = int(input())

for _ in range(n):
    k = input()
    d2[k] = int(input())

res = {k:d1[k]+d2[k] for k in d1}
print(res)
