names = input().split()
marks = list(map(int, input().split()))
lst = list(zip(names, marks))
lst.sort(key=lambda x: x[1], reverse=True)
for i in range(len(lst)):
    print(i+1, lst[i][0], lst[i][1])