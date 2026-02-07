mat = []
row = int(input())
for i in range(row):
    mat.append(list(map(int, input().split())))
mat = list(zip(*mat))
res = []
for i in mat:
    res.append(sum(i))
print(*res)