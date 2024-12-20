s = open("day3.txt").read()

def isNum(s):
    if s == "": return False
    for i in s: 
        if i not in '0123456789': return False
    return True

sum = 0
for i in range(len(s)-8):
    if s[i:i+4] == 'mul(':
        x = 5
        while x < 8:
            if s[i+x] == ',':
                if isNum(s[i+4:i+x]): a = int(s[i+4:i+x])
                break
            x += 1
        if isNum(s[i+4:i+x]):
            y = 2
            while y < 5:
                if s[i+x+y] == ')':
                    if isNum(s[i+x+1:i+x+y]):
                        b = int(s[i+x+1:i+x+y])
                        sum += a*b
                    break
                y += 1
print(sum)

#part 2

sum = 0
do = True
for i in range(len(s)-8):
    if s[i:i+4] == 'do()': do = True
    if s[i:i+7] == "don't()": do = False
    if do:
        if s[i:i+4] == 'mul(':
            x = 5
            while x < 8:
                if s[i+x] == ',':
                    if isNum(s[i+4:i+x]): a = int(s[i+4:i+x])
                    break
                x += 1
            if isNum(s[i+4:i+x]):
                y = 2
                while y < 5:
                    if s[i+x+y] == ')':
                        if isNum(s[i+x+1:i+x+y]):
                            b = int(s[i+x+1:i+x+y])
                            sum += a*b
                        break
                    y += 1
print(sum)