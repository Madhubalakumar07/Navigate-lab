n = int(input())
mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))

p = s = 0
for i in range(n):
    p += mat[i][i]
    s += mat[i][n-i-1]

print(p, s)
