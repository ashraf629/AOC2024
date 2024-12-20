from math import log10, floor

def left(y):
    return y//(10**((floor(log10(y))+1)//2))

def right(y):
    return y%(10**((floor(log10(y))+1)//2))

memo = dict()
def f(a,n):
    if n == 0: return 1
    if (a,n) in memo: return memo[(a,n)]
    if a == 0:
        memo[(a,n)] = f(1,n-1)
        return f(1,n-1)
    elif (floor(log10(a))+1)%2 == 0:
        memo[(a,n)] = f(left(a),n-1) + f(right(a),n-1)
        return f(left(a),n-1) + f(right(a),n-1)
    else:
        memo[(a,n)] = f(2024*a,n-1)
        return f(2024*a,n-1)

with open("day11.txt") as file: nums = list(map(int,file.readline().split(' ')))

blinks = 25
print(sum(map(f,nums,[blinks for _ in range(len(nums))])))

#part 2
blinks=75
print(sum(map(f,nums,[blinks for _ in range(len(nums))])))