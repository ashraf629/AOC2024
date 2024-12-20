grid = [s.strip() for s in open("day20.txt").readlines()]

m,n = len(grid), len(grid[0])
for y in range(m):
    for x in range(n):
        if grid[y][x] == 'S': S = (y,x)

def inBounds(y,x,m,n):
    return -1 < y < m and -1 < x < n

y,x = S
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
track = [S]
t = 0
times = {S:0}
while grid[y][x] != 'E':
    for u,r in dirs:
        if grid[y+u][x+r] != '#' and (y+u,x+r) not in times:
            y = y+u
            x = x+r
            break
    t += 1
    times[(y,x)] = t
    track.append((y,x))

total = 0
for y,x in track:
    for u,r in dirs:
        if grid[y+u][x+r] == '#' and inBounds(y+2*u,x+2*r,m,n) and (y+2*u,x+2*r) in times and times[(y+2*u,x+2*r)] - times[(y,x)] - 2 > 99: total += 1
print(total)

# part 2
# this generalises part 1, just set r = 2 in the square function to get part 1

def square(y,x,m,n):
    r = 20
    out = []
    for i in range(y-r,y+r+1):
        for j in range(x-r,x+r+1):
            if inBounds(i,j,m,n) and abs(i-y)+abs(j-x) <= r: out.append((i,j))
    return out

total = 0
for y,x in track:
    for i,j in square(y,x,m,n):
        if grid[i][j] != '#' and times[(i,j)] - times[(y,x)] - abs(i-y) - abs(j-x) > 99: total+=1
print(total)
