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
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)
    m,n = len(grid), len(grid[0])

    for y in range(m):
        for x in range(n):
            if grid[y][x] == '@': START = (y,x)

    pos = START
    t = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}

    draw_grid(stdscr,grid)

    for s in instructions:
        x = 1
        while grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] == 'O':
            x += 1
        if grid[pos[0]+x*t[s][0]][pos[1]+x*t[s][1]] == '#': continue
        for i in range(x,0,-1):
            grid[pos[0]+i*t[s][0]][pos[1]+i*t[s][1]] = grid[pos[0]+(i-1)*t[s][0]][pos[1]+(i-1)*t[s][1]]
        grid[pos[0]][pos[1]] = '.'
        pos = (pos[0]+t[s][0],pos[1]+t[s][1])
        time.sleep(0.1)
        draw_grid(stdscr,grid)

curses.wrapper(main)