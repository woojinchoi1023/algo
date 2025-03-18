# https://www.acmicpc.net/problem/7576
from collections import deque

N, M = map(int, input().split())

ls = [list(map(int, input().split()))for _ in range(M)]

dist = [[0]*N for _ in range(M)]

d = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def bfs(r, c):
    ori_r, ori_c = r, c
    q = deque()
    q.append((r, c))
    visited = set()
    visited.add((r, c))
    temp = [[0]*N for _ in range(M)]
    # temp[r][c] = 0
    while q:
        r, c = q.popleft()
        # if ls[r][c] == 1:
        #     dist[ori_r][ori_c] = abs(ori_r-r) + abs(ori_c-c)
        #     return True
        for dr, dc in d:
            if -1 < r+dr < M and -1 < c+dc < N and ls[r+dr][c+dc] != -1 and (r+dr, c+dc) not in visited:
                q.append((r+dr, c+dc))
                visited.add((r+dr, c+dc))
                temp[r+dr][c+dc] = temp[r][c] + 1
                if ls[r+dr][c+dc] == 1:
                    dist[ori_r][ori_c] = temp[r+dr][c+dc]
                    return True
    return False


mx = 0
for r in range(M):
    for c in range(N):
        if ls[r][c] == 0 and not bfs(r, c):
            print(-1)
            break
        if dist[r][c] > mx:
            mx = dist[r][c]
    else:
        continue
    break
else:
    print(mx)
# print(dist)
