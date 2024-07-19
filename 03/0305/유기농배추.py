# 1012 유기농배추
from collections import deque


def bfs(r, c):
    q = deque()
    d = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1),
    ]
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            if -1 < r+dr < N and -1 < c+dc < M and ls[r+dr][c+dc]:
                ls[r+dr][c+dc] = 0
                q.append((r+dr, c+dc))


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    ls = [[0]*M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        ls[y][x] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if ls[r][c] == 0:
                continue
            else:
                cnt += 1
                bfs(r, c)
    print(cnt)
