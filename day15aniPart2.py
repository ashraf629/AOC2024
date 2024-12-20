import curses
import time

with open("day15example.txt") as f:
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

def draw_grid(stdscr, grid):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if 0 <= y < height and 0 <= x < width:
                try:
                    stdscr.addch(y, x, cell)
                except curses.error as e:
                    print(f"Error adding character at ({y}, {x}): {cell} - {e}")
    stdscr.refresh()

def main(stdscr):
    global pos
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)
    
    draw_grid(stdscr,grid)
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
        time.sleep(0.1)
        draw_grid(stdscr,grid)

curses.wrapper(main)