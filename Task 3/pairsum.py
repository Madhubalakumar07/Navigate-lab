lst = list(map(int, input().split()))
target = int(input())
count = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target and i < j:
            count += 1
print(count)