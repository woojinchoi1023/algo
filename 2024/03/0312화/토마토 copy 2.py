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

q = deque()

for r in range(M):
    for c in range(N):
        if ls[r][c] == 1:
            q.append((r, c))


while q:
    r, c = q.popleft()

    for dr, dc in d:
        if -1 < r+dr < M and -1 < c+dc < N and ls[r+dr][c+dc] == 0:
            q.append((r+dr, c+dc))
            ls[r+dr][c+dc] = ls[r][c] + 1


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
