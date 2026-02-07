a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(list(set(a) ^ set(b)))
