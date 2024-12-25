with open("day24.txt") as file:
    s = file.readline()
    inputs = dict()
    while s != '\n':
        inputs[s[:3]] = int(s[5])
        s = file.readline()
    s = file.readline()
    connections = []
    while s:
        l = s.split()
        connections.append([l[0],l[1],l[2],l[4][:3]])
        s = file.readline()

# part 2

outputs = dict()
for t in connections:
    outputs[t[3]] = (t[0],t[1],t[2])

"""
for n >= 2:
x_(n-1) AND y_(n-1) = a_(n-1)
x_n XOR y_n = b_n
a_(n-1) OR d_(n-1) = c_n
b_n XOR c_n = z_n
"""
n=2
while n < 45:
    foundA = False
    for t in connections:
        if (t[0],t[1],t[2]) in [('x'+format(n-1,f'0{2}'),'AND','y'+format(n-1,f'0{2}')),('y'+format(n-1,f'0{2}'),'AND','x'+format(n-1,f'0{2}'))]:
            a = t[3]
            foundA = True
    if not foundA:
        print(f'A not found\nn={n}')
        n+=1
        continue
    foundB = False
    for t in connections:
        if (t[0],t[1],t[2]) in [('x'+format(n,f'0{2}'),'XOR','y'+format(n,f'0{2}')),('y'+format(n,f'0{2}'),'XOR','x'+format(n,f'0{2}'))]:
            b = t[3]
            foundB = True
    if not foundB:
        print(f'B not found\nn={n}, a{n-1}={a}')
        print(outputs['z'+format(n,f'0{2}')],'->','z'+format(n,f'0{2}'))
        n+=1
        continue
    foundC = False
    for t in connections:
        if t[1] == 'OR' and (t[0]==a or t[2]==a):
            c = t[3]
            foundC = True
            if t[0] == a: d = t[2]
            else: d = t[0]
    if not foundC:
        print(f'C not found\nn={n}, a{n-1}={a}, b{n}={b}')
        print(outputs['z'+format(n,f'0{2}')],'->','z'+format(n,f'0{2}'))
        n+=1
        continue
    foundZ = False
    for t in connections:
        if (t[0],t[1],t[2]) in [(b,'XOR',c),(c,'XOR',b)]:
            print(t[3])
            z = t[3]
            foundZ = True
    if not foundZ:
        print(f'Z not found\nn={n}, a{n-1}={a}, b{n}={b}, c{n}={c}, d{n-1}={d}')
        print(outputs['z'+format(n,f'0{2}')],'->','z'+format(n,f'0{2}'))
        n+=1
        continue
    if z[0] != 'z': print('z'+format(n,f'0{2}')+' switched with '+z)
    n += 1
# this ends up giving enough information to find out which pairs were swapped

# part 1

loop = True
while connections:
    completed = []
    for t in connections:
        if t[0] in inputs and t[2] in inputs:
            if t[1] == 'AND':
                inputs[t[3]] = inputs[t[0]] and inputs[t[2]]
            elif t[1] == 'OR':
                inputs[t[3]] = inputs[t[0]] or inputs[t[2]]
            else:
                inputs[t[3]] = inputs[t[0]] ^ inputs[t[2]]
            completed.append(t)
    for t in completed:
        connections.remove(t)

output = 0
for z in inputs:
    if z[0] == 'z': output += inputs[z]*2**int(z[1:])
print(output)