s = open("day9.txt").readline().strip()

disk = []
for i in range(0,len(s),2):
    for _ in range(int(s[i])): disk.append(i//2)
    if i+1 < len(s):
        for _ in range(int(s[i+1])): disk.append('.')

i = 0
while i < len(disk):
    if disk[i] != '.':
        i += 1
        continue
    while disk[-1] == '.': disk.pop(-1)
    disk[i] = disk.pop(-1)
    i += 1

checksum = 0
for i in range(len(disk)):
    checksum += i*disk[i]
print(checksum)

# part 2
disk = []
for i in range(0,len(s),2):
    for _ in range(int(s[i])): disk.append(i//2)
    if i+1 < len(s):
        for _ in range(int(s[i+1])): disk.append('.')

blocks = []
x = 0
for i in range(len(s)):
    if i%2 == 0: blocks.append([int(s[i]),x])
    x += int(s[i])

spaces = []
x = 0
for i in range(len(s)):
    if i%2 == 1: spaces.append([int(s[i]),x])
    x += int(s[i])

for i in range(len(blocks)-1,-1,-1):
    for j in range(len(spaces)):
        if spaces[j][0] < blocks[i][0]: continue
        if spaces[j][1] > blocks[i][1]: continue
        for k in range(blocks[i][0]):
            disk[spaces[j][1]+k] = i
            disk[blocks[i][1]+k] = '.'
        spaces[j][0] -= blocks[i][0]
        spaces[j][1] += blocks[i][0]
        break

checksum = 0
for i in range(len(disk)):
    if disk[i] == '.': continue
    checksum += disk[i]*i
print(checksum)
