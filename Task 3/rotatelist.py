lst = list(map(int, input().split()))
k = int(input())
lst = lst[-k:] + lst[:-k]
print(*lst)