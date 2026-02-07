lst = list(map(int, input().split()))
maxlen = curlen = 1

for i in range(1, len(lst)):
    if lst[i] == lst[i-1] + 1:
        curlen += 1
    else:
        curlen = 1
    maxlen = max(maxlen, curlen)

print(maxlen)
