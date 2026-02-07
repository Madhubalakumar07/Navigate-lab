n = int(input())
d = {}

for _ in range(n):
    name = input()
    marks = list(map(int, input().split()))
    d[name] = sum(marks)/len(marks)

print(d)
