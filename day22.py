secrets = [int(x) for x in open('day22.txt').readlines()]

MOD = 16777216
N = 2000

def nextSecret(n):
    n = n^(64*n) % MOD
    n = n^(n//32) % MOD
    n = n^(2048*n) % MOD
    return n

def secretMultiple(secret,n):
    for _ in range(n):
        secret = nextSecret(secret)
    return secret

print(sum(map(secretMultiple,secrets,[N for _ in range(len(secrets))])))

#part 2

allSecrets = []
for secret in secrets:
    l = [secret]
    for _ in range(N):
        l.append(nextSecret(l[-1]))
    l = [x%10 for x in l]
    allSecrets.append(l)
differences = [[x[i+1]-x[i] for i in range(N)] for x in allSecrets]

scores = dict()
for i in range(len(differences)):
    x = 0
    visited = set()
    while x < len(differences[i])-3:
        t = (differences[i][x],differences[i][x+1],differences[i][x+2],differences[i][x+3])
        if t in visited:
            x += 1
            continue
        if t in scores:
            scores[t] += allSecrets[i][x+4]
        else:
            scores[t] = allSecrets[i][x+4]
        visited.add(t)
        x += 1
print(max(scores.values()))
