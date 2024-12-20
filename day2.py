def safe(levels):
    if levels[0] == levels[1]: return False
    sign = (levels[1]-levels[0])//abs(levels[1]-levels[0])
    for i in range(1,len(levels)):
        if not 0 < sign*(levels[i]-levels[i-1]) < 4: return False
    return True

print(sum(map(safe,[[int(x) for x in s.split(' ')] for s in open("day2.txt")])))

#part 2

def safeDamp(levels):
    if safe(levels):return True
    for i in range(len(levels)):
        l = levels[:]
        l.pop(i)
        if safe(l): return True
    return False

print(sum(map(safeDamp,[[int(x) for x in s.split(' ')] for s in open("day2.txt")])))