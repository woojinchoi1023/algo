# https://www.acmicpc.net/problem/20955
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

g = {i: [] for i in range(1, N+1)}
parents = [i for i in range(N+1)]


def findparent(a):
    if parents[a] != a:
        parents[a] = findparent(parents[a])
    return parents[a]


def union(a, b):
    pa, pb = findparent(a), findparent(b)
    if pa == pb:
        return True
    if pa > pb:
        parents[pa] = pb  # 주의!!!
    else:
        parents[pb] = pa
    return False


double = 0
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    if union(u, v):
        double += 1


for i in range(2, N+1):
    findparent(i)


temp = set(parents)
print(len(temp)-2+double)  # 0, 1
