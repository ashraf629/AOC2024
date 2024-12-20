from PIL import Image
import numpy as np

robots = [[(int(s.split(' ')[0].split(',')[0][2:]),int(s.split(' ')[0].split(',')[1])),(int(s.split(' ')[1].split(',')[0][2:]),int(s.split(' ')[1].split(',')[1]))] for s in open("day14.txt").readlines()]

width = 101
height = 103
seconds = 100
grid = [[0 for _ in range(width)] for _ in range(height)]
for r in robots:
    x = (r[0][0] + seconds*r[1][0]) % width
    y = (r[0][1] + seconds*r[1][1]) % height
    grid[y][x] += 1

tl = 0
for y in range(height//2):
    for x in range(width//2):
        tl += grid[y][x]

tr = 0
for y in range(height//2):
    for x in range(width//2 + 1,width):
        tr += grid[y][x]

bl = 0
for y in range(height//2 + 1,height):
    for x in range(width//2):
        bl += grid[y][x]

br = 0
for y in range(height//2 + 1, height):
    for x in range(width//2 + 1, width):
        br += grid[y][x]

print(tl*tr*bl*br)

total_seconds = 10000
for seconds in range(22,total_seconds, 101):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for r in robots:
        x = (r[0][0] + seconds*r[1][0]) % width
        y = (r[0][1] + seconds*r[1][1]) % height
        grid[y][x] = 255
    pixels = np.array(grid, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.save(f'day14images/{seconds}.png')