with open("day10.txt") as f:
    s = f.readline()
    grid = []
    while s:
        grid.append([int(x) for x in s.strip()])
        s = f.readline()

m,n = len(grid),len(grid[0])

zeros = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0: zeros.append((i,j))

sum = 0
for (x,y) in zeros:
    pos = [set() for _ in range(10)]
    pos[0].add((x,y))
    for i in range(9):
        for (a,b) in pos[i]:
            if a > 0 and grid[a-1][b] == i+1: pos[i+1].add((a-1,b))
            if a < m-1 and grid[a+1][b] == i+1: pos[i+1].add((a+1,b))
            if b > 0 and grid[a][b-1] == i+1: pos[i+1].add((a,b-1))
            if b < n-1 and grid[a][b+1] == i+1: pos[i+1].add((a,b+1))
    sum += len(pos[-1])
print(sum)

#part 2

sum = 0
for (x,y) in zeros:
    pos = [[] for _ in range(10)]
    pos[0].append((x,y))
    for i in range(9):
        for (a,b) in pos[i]:
            if a > 0 and grid[a-1][b] == i+1: pos[i+1].append((a-1,b))
            if a < m-1 and grid[a+1][b] == i+1: pos[i+1].append((a+1,b))
            if b > 0 and grid[a][b-1] == i+1: pos[i+1].append((a,b-1))
            if b < n-1 and grid[a][b+1] == i+1: pos[i+1].append((a,b+1))
    sum += len(pos[-1])
print(sum)