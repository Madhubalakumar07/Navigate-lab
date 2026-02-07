n = int(input())
lst = []
for i in range(n):
    tup = tuple(map(int, input().split()))
    lst.append(tup)
res = []
for i in lst:
    key = tuple(sorted(i))
    if key not in res:  
        res.append(key)
print(res)