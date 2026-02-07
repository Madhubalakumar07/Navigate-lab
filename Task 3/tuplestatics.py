lst = list(map(int, input().split()))
res = (max(lst), min(lst), sum(lst)//len(lst))
print(res)