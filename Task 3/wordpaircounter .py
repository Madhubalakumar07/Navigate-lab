words = input().split()
d = {}

for i in range(len(words)-1):
    pair = (words[i], words[i+1])
    d[pair] = d.get(pair,0) + 1

print(d)
