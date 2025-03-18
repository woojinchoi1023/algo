# https://www.acmicpc.net/problem/1005
# 위상 정렬
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    N, K = map(int, input().rstrip().split())
    ls = [0] + list(map(int, input().rstrip().split()))
    g = [[]for _ in range(N+1)]
    in_arrow = [0]*(N+1)
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        g[x].append(y)
        in_arrow[y] += 1

    W = int(input().rstrip())
    dq = deque()
    for i in range(1,N+1):
        if in_arrow[i]==0: # 진입차수 0 인 노드들
            dq.append(i)
    visited = [0]*(N+1)
    while dq:
        curr = dq.popleft()
        for nxt in g[curr]:
            visited[nxt] = max(visited[nxt],visited[curr]+ls[curr])
            in_arrow[nxt] -= 1
            if in_arrow[nxt] == 0: # 0이 되면 큐에 추가
                dq.append(nxt)

    # print(visited)
    print(visited[W]+ls[W])


# N = 1,000
# K = 100,000
# D = 100,000
