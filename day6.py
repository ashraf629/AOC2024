with open("day6.txt") as f:
    grid = []
    s = f.readline()
    while s:
        grid.append(s.strip())
        s = f.readline()

n,m = len(grid[0]),len(grid)
for i in range(m):
    for j in range(n):
        if grid[i][j] == '^': START = (i,j)

def add(v,w):
    return (v[0]+w[0],v[1]+w[1])

guard = START
facing = (-1,0)
positions = set()
positions.add(guard)
while -1<add(guard,facing)[0]<m and -1<add(guard,facing)[1]<n:
    if grid[add(guard,facing)[0]][add(guard,facing)[1]] in ['.','^']:
        guard = add(guard,facing)
        positions.add(guard)
    else:
        facing = (facing[1],-1*facing[0])
print(len(positions))

# part 2

loops = 0
for O in positions:
    if O == START: continue
    guard = START
    facing = (-1,0)
    record = []
    while -1<add(guard,facing)[0]<m and -1<add(guard,facing)[1]<n:
        if grid[add(guard,facing)[0]][add(guard,facing)[1]] == '#' or add(guard,facing) == O:
            if (guard,facing) in record:
                loops += 1
                break
            record.append((guard,facing))
            facing = (facing[1],-1*facing[0])
        else:
            guard = add(guard,facing)
print(loops)
    
    