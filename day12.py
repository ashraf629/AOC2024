grid = [s.strip() for s in open("day12.txt").readlines()]

def clash(block,region,i):
    for p in block:
        if (i-1,p[1]) in region: return True
    return False

def perimeter(region):
    out = 0
    region = set(region)
    for p in region:
        if not (p[0]-1,p[1]) in region: out += 1
        if not (p[0]+1,p[1]) in region: out += 1
        if not (p[0],p[1]-1) in region: out += 1
        if not (p[0],p[1]+1) in region: out += 1
    return out

def edges(region):
    out = 0
    region = set(region)
    for i in range(140):
        p = 0
        while p < 140:
            while p < 140 and (i,p) in region and not (i-1,p) in region: p+=1
            if p > 0: out += 1
            while p < 140 and not((i,p) in region and not (i-1,p) in region): p+=1
    for i in range(140):
        p = 0
        while p < 140:
            while p < 140 and (i,p) in region and not (i+1,p) in region: p+=1
            if p > 0: out += 1
            while p < 140 and not((i,p) in region and not (i+1,p) in region): p+=1
    for i in range(140):
        p = 0
        while p < 140:
            while p < 140 and (p,i) in region and not (p,i-1) in region: p+=1
            if p > 0: out += 1
            while p < 140 and not((p,i) in region and not (p,i-1) in region): p+=1
    for i in range(140):
        p = 0
        while p < 140:
            while p < 140 and (p,i) in region and not (p,i+1) in region: p+=1
            if p > 0: out += 1
            while p < 140 and not((p,i) in region and not (p,i+1) in region): p+=1
    return out


m, n = len(grid), len(grid[0])
sum1 = 0
sum2 = 0
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
count = 0
for c in alphabet:
    regions = []
    for i in range(m):
        p = 0
        row = []
        while p < n:
            block = []
            while p < n and grid[i][p] != c:
                p += 1
            while p < n and grid[i][p] == c:
                block.append((i,p))
                p += 1
            row.append(block)
        for x in range(len(row)):
            indices = []
            for y in range(len(regions)-1,-1,-1):
                if clash(row[x],regions[y],i): indices.append(y)
            region = []
            for y in indices: region += regions.pop(y)
            region += row[x]
            regions.append(region)
    for region in regions:
        if not region: continue
        #part 1
        sum1 += perimeter(region)*len(region)
        #part 2
        sum2 += edges(region)*len(region)
print(sum1)
print(sum2)
