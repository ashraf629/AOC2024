with open("day15.txt") as f:
    s = f.readline()
    grid = []
    while s != '\n':
        grid.append(list(s.strip()))
        s = f.readline()
    instructions = ''
    s = f.readline()
    while s:
        instructions += s.strip()
        s = f.readline()

m,n = len(grid),len(grid[0])

for y in range(m):
    for x in range(n):
        if grid[y][x] == '@': START = (y,x)

pos = START
t = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
for s in instructions:
    x = 1
    while grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] == 'O':
        x += 1
    if grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] == '#': continue
    for i in range(x,0,-1):
        grid[pos[0]+i*t[s][0]][pos[1]+i*t[s][1]] = grid[pos[0]+(i-1)*t[s][0]][pos[1]+(i-1)*t[s][1]]
    grid[pos[0]][pos[1]] = '.'
    pos = (pos[0]+t[s][0],pos[1]+t[s][1])

sum = 0
for y in range(m):
    for x in range(n):
        if grid[y][x] == 'O': sum += 100*y + x
print(sum)

#part 2
with open("day15.txt") as f:
    s = f.readline()
    grid = []
    while s != '\n':
        grid.append(list(s.strip()))
        s = f.readline()
    instructions = ''
    s = f.readline()
    while s:
        instructions += s.strip()
        s = f.readline()

newGrid = []
for row in grid:
    newRow = []
    for s in row:
        if s == '.':
            newRow.append('.')
            newRow.append('.')
        elif s == '#':
            newRow.append('#')
            newRow.append('#')
        elif s == 'O':
            newRow.append('[')
            newRow.append(']')
        else:
            newRow.append('@')
            newRow.append('.')
    newGrid.append(newRow)

grid = newGrid
m,n = len(grid), len(grid[0])

for y in range(m):
    for x in range(n):
        if grid[y][x] == '@': START = (y,x)

pos = START
t = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
for j in range(len(instructions)):
    s = instructions[j]
    if s in ['>','<']:
        x = 1
        while grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] in ['[',']']:
            x += 1
        if grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] == '#': continue
        for i in range(x,0,-1):
            grid[pos[0]+i*t[s][0]][pos[1]+i*t[s][1]] = grid[pos[0]+(i-1)*t[s][0]][pos[1]+(i-1)*t[s][1]]
        grid[pos[0]][pos[1]] = '.'
        pos = (pos[0]+t[s][0],pos[1]+t[s][1])
    else:
        y = pos[0]
        xs = {pos[1]}
        memo = [(y,xs)]
        loop = True
        moveForward = False
        while loop:
            newXs = set()
            for x in xs:
                if grid[y+t[s][0]][x] == '#':
                    loop = False
                    break
                if grid[y+t[s][0]][x] == '[':
                    newXs.add(x)
                    newXs.add(x+1)
                if grid[y+t[s][0]][x] == ']':
                    newXs.add(x)
                    newXs.add(x-1)
            if not loop: continue
            if len(newXs) == 0:
                loop = False
                moveForward = True
                continue
            xs = newXs
            y = y + t[s][0]
            memo.append((y,xs))
        if not moveForward: continue
        for i in range(len(memo)-1,-1,-1):
            y = memo[i][0]
            for x in memo[i][1]:
                grid[y+t[s][0]][x] = grid[y][x]
                grid[y][x] = '.'
        grid[pos[0]][pos[1]] = '.'
        pos = (pos[0]+t[s][0],pos[1])

sum = 0
for y in range(m):
    for x in range(n):
        if grid[y][x] == '[': sum += 100*y + x
print(sum)
