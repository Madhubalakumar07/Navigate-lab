lst = list(map(int, input().split()))
ans = [x for x in lst if lst.count(x) == 1] 
print(*ans)