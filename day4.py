crossword = [x.strip() for x in open("day4.txt").readlines()]

m = len(crossword)
n = len(crossword[0])

#part 1

total = 0

for i in range(m):
    for j in range(n-3):
        if crossword[i][j:j+4] in ['XMAS','SAMX']: total += 1

for i in range(m-3):
    for j in range(n):
        if crossword[i][j] + crossword[i+1][j] + crossword[i+2][j] + crossword[i+3][j] in ['XMAS','SAMX']: total += 1

for i in range(m-3):
    for j in range(n-3):
        if crossword[i][j] + crossword[i+1][j+1] + crossword[i+2][j+2] + crossword[i+3][j+3] in ['XMAS','SAMX']: total += 1

for i in range(m-3):
    for j in range(3,n):
        if crossword[i][j] + crossword[i+1][j-1] + crossword[i+2][j-2] + crossword[i+3][j-3] in ['XMAS','SAMX']: total += 1


print(total)


# part 2

total = 0

for i in range(m-2):
    for j in range(n-2):
        if crossword[i][j] + crossword[i+1][j+1] + crossword[i+2][j+2] in ['MAS','SAM']:
            if crossword[i][j+2] + crossword[i+1][j+1] + crossword[i+2][j] in ['MAS','SAM']: total += 1

print(total)