from math import inf

grid = [s.strip() for s in open("day16.txt").readlines()]

m,n = len(grid), len(grid[0])
spaces = set()
for y in range(m):
    for x in range(n):
        if grid[y][x] in ['.','S','E']: spaces.add((y,x))
        if grid[y][x] == 'S': START = (y,x)
        if grid[y][x] == 'E': END = (y,x)

nodes = dict()
directions = [(1,0),(-1,0),(0,1),(0,-1)]
for (u,r) in directions:
    for (y,x) in spaces:
        nodes[(y,x,u,r)] = [[((y,x,-1*r,u),1000),((y,x,r,-1*u),1000)],inf,[((y,x,-1*r,u),1000),((y,x,r,-1*u),1000)]]
        if (y+u,x+r) in spaces: nodes[(y,x,u,r)][0].append(((y+u,x+r,u,r),1))
        if (y-u,x-r) in spaces: nodes[(y,x,u,r)][2].append(((y-u,x-r,u,r),1))

nodes[(START[0],START[1],0,1)][1] = 0
working_nodes = {(START[0],START[1],0,1)}
visited = {(START[0],START[1],0,1)}
while len(working_nodes) > 0:
    d = inf
    for node in working_nodes:
        if nodes[node][1] < d:
            d = nodes[node][1]
            next = node
    for i in range(len(nodes[next][0])):
        nodes[nodes[next][0][i][0]][1] = min(nodes[nodes[next][0][i][0]][1],nodes[next][0][i][1] + d)
        if not nodes[next][0][i][0] in visited: working_nodes.add(nodes[next][0][i][0])
        visited.add(nodes[next][0][i][0])
    working_nodes.remove(next)

print([nodes[(END[0],END[1],dir[0],dir[1])][1] for dir in directions])

#part 2

path = {END}
now = {(END[0],END[1],-1,0)}
loop = True
while loop:
    next = set()
    loop = False
    for node in now:
        for i in range(len(nodes[node][2])):
            if nodes[node][1] - nodes[node][2][i][1] == nodes[nodes[node][2][i][0]][1]:
                path.add((nodes[node][2][i][0][0],nodes[node][2][i][0][1]))
                next.add(nodes[node][2][i][0])
                loop = True
    now = next
print(len(path))