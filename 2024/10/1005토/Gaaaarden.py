# https://www.acmicpc.net/problem/18809
from collections import deque
N, M, G, R = map(int, input().split())
ls = [list(map(int, input().split()))for _ in range(N)]


yellow = []
for i in range(N):
    for j in range(M):
        if ls[i][j] == 2:
            yellow.append((i, j))

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ans = 0


def bfs(g, r):
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ls[i][j] == 0:
                v[i][j] = 1
    dq = deque()
    for i, j in g:
        v[i][j] = 1
        dq.append((i, j, 2))
    for i, j in r:
        v[i][j] = 1
        dq.append((i, j, 3))

    cnt = 0
    while True:
        new_dq = deque()
        while dq:
            i, j, color = dq.popleft()
            for dr, dc in delta:
                nr, nc = i+dr, j+dc
                if -1 < nr < N and -1 < nc < M and v[nr][nc] != 1:
                    if v[nr][nc] == 0:
                        v[nr][nc] = color
                        new_dq.append((nr, nc, color))
                    elif v[nr][nc] != color:
                        cnt += 1
                        new_dq.remove((nr, nc, v[nr][nc]))  # stop
                        v[nr][nc] = 1
        if new_dq:
            for i, j, color in new_dq:
                v[i][j] = 1
            dq = new_dq
        else:
            break
    return cnt


def dfs(idx: int, g: set, r: set):
    global ans
    if len(g) == G and len(r) == R:
        res = bfs(g, r)
        ans = max(ans, res)
        return
    if idx == len(yellow):
        return
    # pass
    dfs(idx+1, g, r)
    nxt = yellow[idx]
    # green
    if len(g) < G:
        dfs(idx+1, g | {nxt}, r)
    # red
    if len(r) < R:
        dfs(idx+1, g, r | {nxt})


dfs(0, set(), set())
print(ans)
