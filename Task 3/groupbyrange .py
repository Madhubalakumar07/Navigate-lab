lst = list(map(int, input().split()))
d = {"<50":[], "50-74":[], ">=75":[]}

for m in lst:
    if m < 50:
        d["<50"].append(m)
    elif m < 75:
        d["50-74"].append(m)
    else:
        d[">=75"].append(m)

print(d)

