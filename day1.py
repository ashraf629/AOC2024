left, right = sorted([int(s.split('   ')[0]) for s in open("day1.txt")]), sorted([int(s.split('   ')[1]) for s in open("day1.txt")])
print(sum(map(lambda x,y: abs(x-y),left,right)))

#part 2

print(sum(map(lambda x,y : x*y, left, [sum(map(lambda a,b: int(a==b),[x for _ in range(len(left))],right)) for x in left])))