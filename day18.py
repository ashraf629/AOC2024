from math import inf

class DLN:
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __bool__(self):
        if self.head is None: return False
        else: return True

    def append(self,value):
        newNode = DLN(value)
        if self.tail is None:
            self.tail = self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def popHead(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return value

fallingBytes = [(int(s.split(',')[0]),int(s.split(',')[1])) for s in open("day18.txt").readlines()]

grid = [['.' for _ in range(71)] for _ in range(71)]
for (x,y) in fallingBytes[:1028]: grid[y][x] = '#'

spaces = set()
for y in range(71):
    for x in range(71):
        if grid[y][x] == '.': spaces.add((y,x))

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

nodes = dict()
for (y,x) in spaces:
    nodes[(y,x)] = [[],inf]
    for (u,r) in dirs:
        if (y+u,x+r) in spaces: nodes[(y,x)][0].append((y+u,x+r))

# Dijkstra's with no priority queue
nodes[(0,0)][1] = 0
working_nodes = {(0,0)}
visited = {(0,0)}
while len(working_nodes) > 0:
    d = inf
    for node in working_nodes:
        if nodes[node][1] < d:
            d = nodes[node][1]
            next = node
    for i in range(len(nodes[next][0])):
        nodes[nodes[next][0][i]][1] = min(nodes[nodes[next][0][i]][1],1 + d)
        if not nodes[next][0][i] in visited: working_nodes.add(nodes[next][0][i])
        visited.add(nodes[next][0][i])
    working_nodes.remove(next)

print(nodes[(70,70)][1])

#part 2

spaces = set()
for y in range(71):
    for x in range(71):
        if grid[y][x] == '.': spaces.add((y,x))

#Dijkstra
import heapq
import time

startTime = time.time()
for (a,b) in fallingBytes[1028:]:
    spaces.remove((b,a))
    distances = {(0,0):0}
    heap = [(0,(0,0))]
    heapq.heapify(heap)
    visited = set()
    while heap:
        d,(y,x) = heapq.heappop(heap)
        if (y,x) in visited: continue
        visited.add((y,x))
        for u,r in dirs:
            if (y+u,x+r) in spaces:
                if (y+u,x+r) not in distances:
                    distances[(y+u,x+r)] = d+1
                    heapq.heappush(heap,(d+1,(y+u,x+r)))
                if d+1 < distances[(y+u,x+r)]:
                    heapq.heappush((d+1,(y+u,x+r)))
                    distances[(y+u,x+r)] = d+1
    if (70,70) not in distances:
        print(a,b)
        print(f"time taken with Dijkstra's: {time.time() - startTime}")
        break

spaces = set()
for y in range(71):
    for x in range(71):
        if grid[y][x] == '.': spaces.add((y,x))

#BFS
startTime = time.time()
for (a,b) in fallingBytes[1028:]:
    spaces.remove((b,a))
    queue = DLL()
    queue.append((0,0,0))
    visited = {(0,0)}
    distances = dict()
    while queue:
        y,x,d = queue.popHead()
        distances[(y,x)] = d
        for (u,r) in dirs:
            if (y+u,x+r) not in spaces or (y+u,x+r) in visited: continue
            queue.append((y+u,x+r,d+1))
            visited.add((y+u,x+r))
    if (70,70) not in distances:
        print(a,b)
        print(f"time taken with breadth first search: {time.time() - startTime}")
        break
