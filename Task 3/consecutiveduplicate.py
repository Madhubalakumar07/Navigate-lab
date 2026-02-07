lst = list(map(int, input().split()))
lst = [x for i, x in enumerate(lst) if i == 0 or x != lst[i-1]]
print(lst)