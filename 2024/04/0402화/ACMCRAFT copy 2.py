# https://www.acmicpc.net/problem/1005
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    N, K = map(int, input().rstrip().split())
    ls = [0] + list(map(int, input().rstrip().split()))
    g = [[]for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        g[y].append(x)

    W = int(input().rstrip())
    dq = deque()
    dq.append(W)
    visited = [0]*(N+1)
    visited[W] = ls[W]
    while dq:
        curr = dq.popleft()
        for p in g[curr]:
            if visited[p] < visited[curr]+ls[p]:
                visited[p] = visited[curr]+ls[p]
                dq.append(p)

    # print(g)
    print(max(visited))


# N = 1,000
# K = 100,000
# D = 100,000
