# https://www.acmicpc.net/problem/5547

from collections import deque
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
ls = [[0]*W for _ in range(H)]
for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(8):
        if temp[j]:
            ls[i][j] = 1
print(*ls, sep='\n')

d = [
    (-1, 0),
    (0, -1),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
]


def bfs(r, c):
    dq = deque()
    dq.append((r, c))
    visited = [[0]*W for _ in range(H)]
    visited[r][c] = 1
    while dq:
        for dr, dc in d:
            if -1 < r+dr < H and -1 < c+dc < W and ls[r+dr][c+dc] and visited[r+dr][c+dc] == 0:
                visited[r+dr][c+dc] = 1
                dq.append()
