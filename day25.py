keys = []
locks = []
for s in open("day25.txt").read().split('\n\n'):
    rows = s.split('\n')
    nums = [sum(map(lambda x: x=='#',[rows[j][i] for j in range(7)]))-1 for i in range(5)]
    if rows[0][0] == '.': keys.append(nums)
    else: locks.append(nums)

total = 0
for k in keys:
    for l in locks:
        overlap = False
        for i in range(5):
            if k[i]+l[i]>5:
                overlap = True
                break
        if not overlap: total += 1
print(total)