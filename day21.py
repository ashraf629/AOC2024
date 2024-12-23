from math import inf

codes = [s.strip() for s in open("day21.txt").readlines()]
coords = {'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1),'3':(2,2),'0':(3,1),'A':(3,2)}
dirs = {(1,0):(1,1),(-1,0):(0,1),(0,1):(1,2),(0,-1):(1,0)}

def sign(n):
    return n//abs(n)

def directPath(s,e):
    if s == e : return []
    if s[0] == e[0]:
        return [dirs[(0,sign(e[1]-s[1]))] for _ in range(abs(e[1]-s[1]))]
    if s[1] == e[1]:
        return [dirs[(sign(e[0]-s[0]),0)] for _ in range(abs(e[0]-s[0]))]

def allPaths(s,e):
    if s == e: return [[(0,2)]]
    if s[0] == e[0]:
        return [directPath(s,e)+[(0,2)]]
    if s[1] == e[1]:
        return [directPath(s,e)+[(0,2)]]
    return [directPath(s,(s[0],e[1]))+directPath((s[0],e[1]),e)+[(0,2)],directPath(s,(e[0],s[1]))+directPath((e[0],s[1]),e)+[(0,2)]] 

def padOnePaths(start,end):
    if start == (3,1) and end[1] == 0:
        l = allPaths(start,end)
        for x in l:
            if x[0] == (1,0):
                l.remove(x)
                return(l)
    if start == (3,2) and end[1] == 0:
        l = allPaths(start,end)
        for x in l:
            if x[0:2] == [(1,0),(1,0)]:
                l.remove(x)
                return l
    if start == (2,0) and end[0] == 3:
        l = allPaths(start,end)
        for x in l:
            if x[0] == (1,1):
                l.remove(x)
                return l
    if start == (1,0) and end[0] == 3:
        l = allPaths(start,end)
        for x in l:
            if x[0:2] == [(1,1),(1,1)]:
                l.remove(x)
                return l
    if start == (0,0) and end[0] == 3:
        l = allPaths(start,end)
        for x in l:
            if x[0:3] == [(1,1),(1,1),(1,1)]:
                l.remove(x)
                return l
    return allPaths(start,end)

def padTwoPaths(start,end):
    if start[1] == 0 and end[0] == 0:
        l = allPaths(start,end)
        for x in l:
            if x[0] == (0,1):
                l.remove(x)
                return(l)
    if start == (0,1) and end[1] == 0:
        l = allPaths(start,end)
        for x in l:
            if x[0] == (1,0):
                l.remove(x)
                return l
    if start == (0,2) and end[1] == 0:
        l = allPaths(start,end)
        for x in l:
            if x[0:2] == [(1,0),(1,0)]:
                l.remove(x)
                return l
    return allPaths(start,end)

memo = dict() # if depth >= 10, this gets quite slow without memoisation
def l(a,b,d):
    # returns length of shortest input for robot d+1 to make robot 1 move from a to b and push b, where a and b are on pad 2
    if d == 1:
        return len(padTwoPaths(a,b)[0])
    if (a,b,d) in memo: return memo[(a,b,d)]
    paths = padTwoPaths(a,b)
    minLen = inf
    for p in paths:
        minLen = min(minLen,l((0,2),p[0],d-1)+sum([l(p[i],p[i+1],d-1) for i in range(len(p)-1)]))
    memo[(a,b,d)] = minLen
    return minLen

def shortSeq(code,depth):
    # DFS to traverse all possible inputs for robot 0
    code = [coords[x] for x in code]
    root = ((3,2),-1,[])
    stack = [root]
    minLength = inf
    while stack:
        start, index, path = stack.pop()
        if index == len(code)-1:
            length = l((0,2),path[0],depth) + sum([l(path[i],path[i+1],depth) for i in range(len(path)-1)])
            minLength = min(minLength,length)
            continue
        end = code[index+1]
        for p in padOnePaths(start,end):
            stack.append((end,index+1,path+p))
    return minLength

print(sum([int(code[:-1])*shortSeq(code,2) for code in codes]))
print(sum([int(code[:-1])*shortSeq(code,25) for code in codes]))