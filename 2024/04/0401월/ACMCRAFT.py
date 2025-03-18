# https://www.acmicpc.net/problem/1005
# from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    N, K = map(int, input().rstrip().split())
    ls = [0] + list(map(int, input().rstrip().split()))
    g = {
        i: {}for i in range(N+1)
    }
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        g[y][x] = ls[x]

    W = int(input().rstrip())
    dq = deque()
    dq.append(W)
    visited = [0]*(N+1)
    visited[W] = ls[W]
    while dq:
        curr = dq.popleft()
        for p, w in g[curr].items():
            if visited[p] < visited[curr]+w:
                visited[p] = visited[curr]+w
                dq.append(p)

    print(g)
    print(visited)
