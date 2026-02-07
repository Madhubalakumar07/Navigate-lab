req = eval(input())
cand = eval(input())

score = 0
for k in req:
    if k in cand:
        score += req[k] * cand[k]

print(score)
