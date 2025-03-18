# https://www.acmicpc.net/problem/7576
from collections import deque
# import sys
# input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())

ls = [list(map(int, input().rstrip('\n').split()))for _ in range(M)]


d = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

first = []
for r in range(M):
    for c in range(N):
        if ls[r][c] == 1:
            first.append((r, c))


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited = set()
    visited.add((r, c))
    while q:
        r, c = q.popleft()

        for dr, dc in d:
            if -1 < r+dr < M and -1 < c+dc < N and ls[r+dr][c+dc] not in [-1, 1] and (r+dr, c+dc) not in visited:
                if 1 < ls[r+dr][c+dc] <= ls[r][c] + 1:  # 기존 값이 더 작다
                    continue
                q.append((r+dr, c+dc))
                visited.add((r+dr, c+dc))
                ls[r+dr][c+dc] = ls[r][c] + 1
    return


for r, c in first:
    bfs(r, c)

mx = 0
for i in ls:
    for j in i:
        if j == 0:
            mx = -1
            break
        elif j-1 > mx:
            mx = j-1
    else:
        continue
    break
print(mx)
