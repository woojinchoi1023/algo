# https://www.acmicpc.net/problem/2638
from collections import deque
N, M = map(int, input().split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if ls[i][j] == 1:
            ls[i][j] = 2

visited = [[0]*M for _ in range(N)]

d = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def sol(air: deque):
    melt = deque()
    while air:
        r, c = air.popleft()
        visited[r][c] = 1
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < M and not visited[nr][nc]:
                if ls[nr][nc] == 2:  # 최초로 공기 닿으면 2->1
                    ls[nr][nc] = 1
                elif ls[nr][nc] == 1:
                    ls[r][c] = 0
                    melt.append((nr, nc))
                    visited[nr][nc] = 1
                else:
                    air.append((nr, nc))
                    visited[nr][nc] = 1
    return melt


air = deque()
air.append((0, 0))
cnt = 0
air = sol(air)
while air:
    cnt += 1
    air = sol(air)
print(cnt)
