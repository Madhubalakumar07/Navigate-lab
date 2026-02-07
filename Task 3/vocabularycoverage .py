expected = set(input().split())
docs = input().split()

used = set(docs)
covered = expected & used

print((len(covered)/len(expected))*100)
print(expected-used)
