# https://www.acmicpc.net/problem/2638
from collections import deque
N, M = map(int, input().split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))


d = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
air = deque()
air.append((0, 0))


def bfs(air: deque):
    melt = deque()
    while air:
        r, c = air.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                if ls[nr][nc] == 1:
                    cnt = 0
                    for dr, dc in d:
                        nnr, nnc = nr+dr, nc+dc
                        if -1 < nnr < N and -1 < nnc < M and ls[nnr][nnc] == 0:
                            cnt += 1
                    if cnt >= 2:
                        melt.append((nr, nc))
                else:
                    air.append((nr, nc))
    print(melt)
    for r, c in melt:
        ls[r][c] = 0
    return melt


melt = bfs(air)
melt = bfs(melt)
