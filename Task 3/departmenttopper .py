n = int(input())
res = {}

for _ in range(n):
    name = input()
    dept = input()
    marks = int(input())

    if dept not in res or marks > res[dept][1]:
        res[dept] = (name, marks)

print(res)
