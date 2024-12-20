with open("day8.txt") as f:
    s = f.readline()
    grid = []
    while s:
        grid.append(s.strip())
        s = f.readline()

m,n = len(grid),len(grid[0])
antinodes = set()
for x in range(n*m-1):
    if grid[x//n][x%n] == '.': continue
    for y in range(x+1,n*m):
        if grid[y//n][y%n] != grid[x//n][x%n]: continue
        if -1<2*(x//n)-y//n<m and -1<2*(x%n)-y%n<n:
            antinodes.add((2*(x//n)-y//n,2*(x%n)-y%n))
        if -1<2*(y//n)-x//n<m and -1<2*(y%n)-x%n<n:
            antinodes.add((2*(y//n)-x//n,2*(y%n)-x%n))
print(len(antinodes))

#part 2

from math import gcd

def add(v,w):
    return((v[0]+w[0],v[1]+w[1]))

def inbounds(v,m,n):
    return -1<v[0]<m and -1<v[1]<n

def mul(k,v):
    return ((k*v[0],k*v[1]))

for x in range(n*m-1):
    if grid[x//n][x%n] == '.': continue
    for y in range(x+1,n*m):
        if grid[y//n][y%n] != grid[x//n][x%n]: continue
        X = (x//n,x%n)
        Y = (y//n,y%n)
        grad = ((X[0]-Y[0])//gcd(X[0]-Y[0],X[1]-Y[1]),(X[1]-Y[1])//gcd(X[0]-Y[0],X[1]-Y[1]))
        i = 0
        while inbounds(add(X,mul(i,grad)),m,n):
            antinodes.add(add(X,mul(i,grad)))
            i += 1
        i = -1
        while inbounds(add(X,mul(i,grad)),m,n):
            antinodes.add(add(X,mul(i,grad)))
            i -= 1

print(len(antinodes))
