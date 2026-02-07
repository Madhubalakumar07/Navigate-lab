r = int(input())
c = int(input())
flag = True

for _ in range(r):
    row = list(map(int, input().split()))
    if len(row) != len(set(row)):
        flag = False

print(flag)
