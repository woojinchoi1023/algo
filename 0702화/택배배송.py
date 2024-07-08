# https://www.acmicpc.net/problem/5972
import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
g = {
    i: []for i in range(1, N+1)
}
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
# print(g)


def dijk(s):
    dist = [float('inf')]*(N+1)
    dist[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))  # d, curr
    while hq:
        d, curr = heapq.heappop(hq)
        for child, cost in g[curr]:
            if cost+d < dist[child]:
                dist[child] = cost+d
                heapq.heappush(hq, (cost+d, child))
    return dist


dist = dijk(1)
# print(dist)
print(dist[N])
