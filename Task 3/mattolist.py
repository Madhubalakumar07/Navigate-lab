mat = []
row = int(input())
for i in range(row):
    mat.append(list(map(int, input().split())))
print(mat)
res = []
for i in mat:
    for j in i:
        res.append(j)
print(res)