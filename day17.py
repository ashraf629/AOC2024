with open("day17.txt") as file:
    A = int(file.readline().split(' ')[2])
    B = int(file.readline().split(' ')[2])
    C = int(file.readline().split(' ')[2])
    file.readline()
    program = [int(x) for x in file.readline().split(' ')[1].split(',')]

def compile(A,B,C,program):
    out = []
    p = 0
    while p < len(program)-1 and len(out) <= len(program):
        if program[p] == 0:#adv
            A = A // 2**[0,1,2,3,A,B,C][program[p+1]]
        elif program[p] == 1:#bxl
            B = B^program[p+1]
        elif program[p] == 2:#bst
            B = [0,1,2,3,A,B,C][program[p+1]] % 8
        elif program[p] == 3:#jnz
            if A != 0:
                p = program[p+1] - 2
        elif program[p] == 4:#bxc
            B = B^C
        elif program[p] == 5:#out
            out.append([0,1,2,3,A,B,C][program[p+1]] % 8)
        elif program[p] == 6:#bdv
            B = A // 2**[0,1,2,3,A,B,C][program[p+1]]
        elif program[p] == 7:#cdv
            C = A // 2**[0,1,2,3,A,B,C][program[p+1]]
        p += 2
    return out

print(compile(A,B,C,program))

# part 2
# this part involves first figuring out what the program in the puzzle input actually does

possible = []
#yikes!
for i in range(len(program)-1,-1,-1):
    out = program[i]
    l = []
    for b in range(8):
        A = ['*' for _ in range(3*19)]
        bb = format(b,f'0{3}b')
        for j in range(3):
            A[3*i+j] = bb[2-j]
        c = format(out^7^b^2,f'0{3}b')
        clash = False
        for j in range(3):
            if A[3*i+(b^2)+j] != '*' and A[3*i+(b^2)+j] != c[2-j]: clash = True
        if not clash:
            for j in range(3):
                A[3*i+(b^2)+j] = c[2-j]
            l.append(''.join(A[::-1]))
    possible.append(l)

cand = ''.join(['0' for _ in range(3*3)] + ['*' for _ in range(3*16)])

def compatible(s,cand):
    for i in range(len(s)):
        if s[i] == '*' or cand[i] == '*': continue
        if s[i] != cand[i]: return False
    return True

def joinStr(s,cand):
    new = list(cand)
    for i in range(len(s)):
        if s[i] != '*': new[i] = s[i]
    return ''.join(new)

#DFS
node = ''.join(['0' for _ in range(3*3)] + ['*' for _ in range(3*16)])
stack = [node]
visited = {node}
while stack:
    s = stack.pop()
    x = 0
    while x < 3*19 and s[x] != '*':
        x += 1
    x = x // 3 - 3
    if x == 16:
        A = int(s,2)
        break
    for y in possible[x][::-1]:
        cand = joinStr(y,s)
        if compatible(y,s) and cand not in visited:
            stack.append(cand)
            visited.add(cand)

print(compile(A,B,C,program))
print(A)