# https://www.acmicpc.net/problem/13549
from collections import deque
N, K = map(int, input().split())
visited = [100000] * 100000


def bfs(start):
    global K
    dq = deque()
    while start < 100000:
        dq.append(start)
        visited[start] = 0
        start *= 2

    while dq:
        curr = dq.popleft()
        temp = curr
        while temp < 100000:
            dq.append(temp)
            visited[temp] = visited[curr]
            temp *= 2
        cand = [(t, x) for t, x in [(1, curr+1), (1, curr-1),
                                    ] if -1 < x < 100000]
        temp = []
        for t, x in cand:
            visited[x] = min(visited[x], visited[curr]+t)
            temp.append(x)
        if visited[K] != 100000:
            return visited[K]
        dq.extend(temp)


print(bfs(N))
