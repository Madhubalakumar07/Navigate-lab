req = set(input().split())
stu = set(input().split())

print("Missing:", req-stu)
print("Extra:", stu-req)
