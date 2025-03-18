# https://www.acmicpc.net/problem/1197
from heapq import heappop, heappush
V, E = map(int, input().split())
g = {i: {}for i in range(V+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].update({b: c})
    g[b].update({a: c})

# print(g)


def prim():
    cnt = 0
    visited = [0]*(V+1)
    q = []
    heappush(q, [0, 1])
    while q:
        w, curr = heappop(q)
        if visited[curr]:
            continue
        cnt += w
        visited[curr] = 1
        for e, dis in g[curr].items():
            if not visited[e]:
                heappush(q, [dis, e])
    return cnt


print(prim())
