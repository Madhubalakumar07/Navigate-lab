data = list(map(int, input().split()))
remove = list(map(int, input().split()))

res = [x for x in data if x not in remove]
print(res)
