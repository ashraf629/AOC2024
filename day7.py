with open("day7.txt") as f:
    s = f.readline()
    puzzle = []
    while s:
        puzzle.append((int(s.split(':')[0]),[int(x) for x in s.split(':')[1].strip().split(' ')]))
        s = f.readline()

total = 0
for (value,nums) in puzzle:
    for i in range(2**(len(nums)-1)):
        sum = nums[0]
        for j in range(len(nums)-1):
            if format(i,f'0{len(nums)-1}b')[j] == '0':
                sum += nums[j+1]
            else:
                sum *= nums[j+1]
        if value == sum:
            total += value
            break

print(total)

#part 2

def ternary(n,d):
    s = ''
    while n//3 > 0:
        s = str(n%3) + s
        n = n//3
    s = str(n%3) + s
    for _ in range(d-len(s)):
        s = '0' + s
    return s

total = 0
for (value,nums) in puzzle:
    for i in range(3**(len(nums)-1)):
        sum = nums[0]
        for j in range(len(nums)-1):
            if ternary(i,len(nums)-1)[j] == '0':
                sum += nums[j+1]
            elif ternary(i,len(nums)-1)[j] == '1':
                sum *= nums[j+1]
            else:
                sum = int(str(sum)+str(nums[j+1]))
            if sum > value: break
        if value == sum:
            total += value
            break

print(total)