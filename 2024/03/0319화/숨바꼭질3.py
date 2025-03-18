# https://www.acmicpc.net/problem/13549
# 시간초과
from collections import deque
N, K = map(int, input().split())
visited = [100000] * 100000


def bfs(start):
    global K
    dq = deque()
    dq.append(start)
    visited[start] = 0
    while dq:
        curr = dq.popleft()
        cand = [(t, x) for t, x in [(1, curr+1), (1, curr-1),
                                    (0, curr*2)] if -1 < x < 100000]
        temp = []
        for t, x in cand:
            visited[x] = min(visited[x], visited[curr]+t)
            temp.append(x)
        if K in temp:
            return visited[K]
        dq.extend(temp)


print(bfs(N))
