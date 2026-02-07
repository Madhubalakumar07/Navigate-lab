a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = False
for i in range(len(a)):
    if b == a[i:] + a[:i]:
        res = True

print(res)
