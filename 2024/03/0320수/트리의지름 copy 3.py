# https://www.acmicpc.net/problem/1967

N = int(input())
g = {}
k = {}
parent = []
for i in range(N-1):
    p, c, w = map(int, input().split())
    k.setdefault(c, [])
    k[c].append((p, w))
    g.setdefault(p, [])
    g[p].append((c, w))
    parent.append(p)
# child : parent
leaf = [i for i in range(1, N+1) if i not in parent]

d = {}
print(g)
print(k)
for i in range(N, -1, -1):
    child = g.get(i, [])
    cand = []
