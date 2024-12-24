with open("day5.txt") as f:
    s = f.readline()
    rules = []
    while s != '\n':
        rules.append([int(x) for x in s.strip().split('|')])
        s = f.readline()
    s = f.readline()
    updates = []
    while s != '':
        updates.append([int(x) for x in s.strip().split(',')])
        s = f.readline()

def check(update,rules):
    for x in range(len(update)):
        for y in rules:
            if y[0] == update[x] and y[1] in update[:x]:
                return False
    return True

sum = 0

for update in updates:
    if check(update,rules):
        sum += update[len(update)//2]

print(sum)

# part 2
# using a DFS-based topological sorting algorithm

def topologicalSortUtil(v,adj,stack,visited):
    visited.add(v)
    for w in adj[str(v)]:
        if w not in visited:
            topologicalSortUtil(w,adj,stack,visited)
    stack.append(v)

def topologicalSort(nodes,adj):
    stack = []
    visited = set()
    for node in nodes:
        if node not in visited:
            visited.add(node)
            for v in adj[str(node)]:
                if v not in visited:
                    topologicalSortUtil(v,adj,stack,visited)
            stack.append(node)
    return stack[::-1]

total = 0
for update in updates:
    if check(update,rules):
        continue
    adj = {str(x):[] for x in update}
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            adj[str(rule[0])].append(rule[1])
    update = topologicalSort(update,adj)
    total += update[len(update)//2]
print(total)

# original version

from copy import copy

def move(x,y,l):# move l[x] into position y
    if x < y:
        temp = l[x]
        for i in range(x,y):
            l[i] = l[i+1]
        l[y] = temp
    if y < x:
        temp = l[x]
        for i in range(x,y,-1):
            l[i] = l[i-1]
        l[y] = temp

working = [[] for _ in range(100)]
for x in rules:
    working[x[0]].append(x[1])

sum = 0
for update in updates:
    if not check(update,rules):
        ucopy = copy(update)
        for i in update:
            ind = len(update)
            if working[i]:
                for x in working[i]:
                    if x in update: ind = min(ind,ucopy.index(x))
            x = ucopy.index(i)
            if x > ind:
                move(x,ind,ucopy)
        sum += ucopy[len(update)//2]

print(sum)
