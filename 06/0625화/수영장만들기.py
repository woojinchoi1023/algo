# https://www.acmicpc.net/problem/1113
import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().rstrip('\n'))))

# print(*ls, sep='\n')

hq = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if ls[i][j] == 9:
            continue
        heapq.heappush(hq, [ls[i][j], i, j])

d = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def check(h, r, c):
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    dq = deque()

    for dr, dc in d:
        if -1 < r+dr < N and -1 < c+dc < M:
            dq.append((r+dr, c+dc))
        else:
            return 0

    while dq:
        # print(dq)
        r, c = dq.popleft()
        visited[r][c] = 1
        if ls[r][c] < h+1:
            for dr, dc in d:
                if -1 < r+dr < N and -1 < c+dc < M:
                    if not visited[r+dr][c+dc]:
                        dq.append((r+dr, c+dc))
                else:
                    return 0
    return 1


cnt = 0
while hq:
    # print(hq)
    h, r, c = heapq.heappop(hq)

    temp = check(h, r, c)

    if temp:
        ls[r][c] += 1
        cnt += 1
        if ls[r][c] != 9:
            heapq.heappush(hq, [ls[r][c], r, c])
print(cnt)
