# https://www.acmicpc.net/problem/14940
from collections import deque

N, M = map(int, input().split())
ls = list(list(map(int, input().split()))for i in range(N))
ans = [[0]*M for i in range(N)]


def bfs(r, c):
    delta = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    q = deque()
    q.append((r, c))

    ls[r][c] = 0
    visited = set()
    while q:

        r, c = q.popleft()
        for dr, dc in delta:
            if -1 < r+dr < N and -1 < c+dc < M and ls[r+dr][c+dc] == 1 and (r+dr, c+dc) not in visited:
                ans[r+dr][c+dc] = ans[r][c]+1
                visited.add((r+dr, c+dc))
                q.append((r+dr, c+dc))


for r in range(N):
    for c in range(M):
        if ls[r][c] == 2:
            break
    else:
        continue
    break
bfs(r, c)
for i in range(N):
    for j in range(M):
        if (i, j) != (r, c) and ls[i][j] == 1 and ans[i][j] == 0:
            ans[i][j] = -1
for i in ans:
    print(*i)
# print(ans)
