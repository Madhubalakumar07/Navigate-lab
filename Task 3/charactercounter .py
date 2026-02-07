s = input()
res = {"alphabets":0,"digits":0,"special":0}

for c in s:
    if c.isalpha():
        res["alphabets"] += 1
    elif c.isdigit():
        res["digits"] += 1
    else:
        res["special"] += 1

print(res)
