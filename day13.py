from sympy import gcdex, floor, ceiling

with open("day13.txt") as f:
    s = f.readline()
    games = []
    while s:
        game = []
        s = s.split(' ')
        A = (int(s[2].split('+')[1][:-1]),int(s[3].split('+')[1]))
        game.append(A)
        s = f.readline()
        s = s.split(' ')
        B = (int(s[2].split('+')[1][:-1]),int(s[3].split('+')[1]))
        game.append(B)
        s = f.readline()
        s = s.split(' ')
        P = (int(s[1].split('=')[1][:-1]),int(s[2].split('=')[1]))
        game.append(P)
        s = f.readline()
        s = f.readline()
        games.append(game)


def cost(game):
    [A,B,P] = game
    ax, ay = A
    bx, by = B
    X, Y = P
    det = ax*by-bx*ay
    if det != 0:
        n = by*X-bx*Y
        m = ax*Y-ay*X
        if n % det != 0 or m % det != 0 or n*det < 0 or m*det < 0: return 0
        return (3*n + m) // det
    # the following deals with a more general case which isn't included in the puzzle input
    if ax*Y != ay*X:
        return 0
    d, n, m = gcdex(ax,bx)
    if floor(m*d/ax) < ceiling(-1*n*d/bx): return 0
    if 3*bx-ax > 0: return X*((3*bx-ax)*floor(-1*n*d/bx)//d + 3*n + m)//d
    else: return X*((3*bx-ax)*ceiling(m*d/ax)//d + 3*n + m)//d

print(sum(map(cost,games)))

#part 2

with open("day13.txt") as f:
    s = f.readline()
    games = []
    while s:
        game = []
        s = s.split(' ')
        A = (int(s[2].split('+')[1][:-1]),int(s[3].split('+')[1]))
        game.append(A)
        s = f.readline()
        s = s.split(' ')
        B = (int(s[2].split('+')[1][:-1]),int(s[3].split('+')[1]))
        game.append(B)
        s = f.readline()
        s = s.split(' ')
        P = (10000000000000+int(s[1].split('=')[1][:-1]),10000000000000+int(s[2].split('=')[1]))
        game.append(P)
        s = f.readline()
        s = f.readline()
        games.append(game)

print(sum(map(cost,games)))