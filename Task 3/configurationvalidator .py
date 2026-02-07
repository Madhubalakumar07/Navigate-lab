conf = eval(input())
req = set(input().split())

print("Missing:", req-conf.keys())
print("Extra:", conf.keys()-req)
