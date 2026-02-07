n = int(input())
vocab = set()

for _ in range(n):
    s = input().split()
    vocab.update(s)

print(vocab)
