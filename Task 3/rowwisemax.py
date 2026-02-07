mat = []
row = int(input())
res = []
for i in range(row):
    mat.append(list(map(int, input().split())))
for i in mat:
    res.append(max(i))
print(*res) 