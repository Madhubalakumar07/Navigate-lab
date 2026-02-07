lst = list(map(int, input().split()))
for i in range(len(lst)-1):
    if lst[i] > max(lst[i+1:]):
        print(lst[i], end=' ')
print(lst[-1])