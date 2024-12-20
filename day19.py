with open("day19.txt") as file:
    towels = [s.strip() for s in file.readline().split(',')]
    file.readline()
    patterns = [s.strip() for s in file.readlines()]

class LN:
    def __init__(self,value,pointer):
        self.value = value
        self.pointer = pointer
    
    def __bool__(self):
        return True

total = 0
for pattern in patterns:
    stack = [LN('',None)]
    visited = set()
    memo = {'':0}
    while stack:
        s = stack.pop()
        if s.value in visited:
            total += memo[s.value]
            n = s.pointer
            while n:
                memo[n.value] += memo[s.value]
                n = n.pointer
            continue
        visited.add(s.value)
        for t in towels:
            if len(s.value+t) <= len(pattern) and s.value+t == pattern[:len(s.value+t)]:
                stack.append(LN(s.value+t,s))
                if s.value+t not in memo: memo[s.value+t] = 0
                if s.value+t == pattern:
                    total += 1
                    n = s
                    while n:
                        memo[n.value] += 1
                        n = n.pointer
                    # include this for part 1
                    #stack = []
                    #break

print(total)
