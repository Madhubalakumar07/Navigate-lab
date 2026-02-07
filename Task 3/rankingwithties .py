scores = list(map(int, input().split()))
rank = []
r = 1

for i in range(len(scores)):
    if i > 0 and scores[i] < scores[i-1]:
        r = i + 1
    rank.append(r)

print(rank)
