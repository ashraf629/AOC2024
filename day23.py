edges = [s.strip().split('-') for s in open("day23.txt").readlines()]
graph = dict()
for e in edges:
    for x in range(2):
        if e[x] in graph:
            graph[e[x]].append(e[1-x])
        else:
            graph[e[x]] = [e[1-x]]
count = 0
for comp in graph:
    if len(graph[comp]) < 2: continue
    for i in range(len(graph[comp])-1):
        for j in range(i+1,len(graph[comp])):
            if graph[comp][j] in graph[graph[comp][i]] and (comp[0] == 't' or graph[comp][j][0] == 't' or graph[comp][i][0] == 't'): count += 1
print(count//3)

# part 2
# This part is solving the clique problem which is NP hard!
"""
y = [len(graph[comp]) for comp in graph]
print(y)
"""
# Each computer is connected to exactly 13 others

def complete(computers):
    if len(computers) < 2: return True
    for i in range(len(computers)-1):
        for j in range(i+1,len(computers)):
            if computers[i] not in graph[computers[j]]: return False
    return True

# looking for a complete subgraph with 14 nodes
"""
for computers in graph.values():
    if complete(computers):
        print(','.join(sorted(computers)))
"""
# there are no complete subgraphs with 14 nodes

# looking for a complete subgraph with 13 nodes
stop = False
for comp in graph:
    for i in range(len(graph[comp])-1):
        if complete(graph[comp][:i]+graph[comp][i+1:]):
            print(','.join(sorted([comp]+graph[comp][:i]+graph[comp][i+1:])))
            stop = True
            break
    if stop: break
    if complete(graph[comp][:-1]):
        print(','.join(sorted([comp]+graph[comp][:i]+graph[comp][i+1:])))
        break