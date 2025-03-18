# https://www.acmicpc.net/problem/1113
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().rstrip('\n').rstrip(' '))))


d = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def check(r, c):
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    dq = deque()
    dq.append((r, c))
    wall = 11  # 벽 최소 높이
    area = []  # 물 넣을 영역
    water = 0  # 물 최고 높이
    while dq:
        r, c = dq.popleft()
        water = max(water, ls[r][c])
        area.append((r, c))
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < M:
                if not visited[nr][nc]:
                    if ls[nr][nc] <= water:
                        dq.append((nr, nc))
                        visited[nr][nc] = 1  # 최단거리 구하는게 아니니까
                    else:
                        wall = min(wall, ls[nr][nc])
            else:  # 바깥으로 나가는 경우
                return [], wall
    return area, wall


checked = [[0]*M for _ in range(N)]
cnt = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if not checked[i][j] and ls[i][j] != 9:
            area, wall = check(i, j)
            for r, c in area:
                checked[r][c] = 1
                cnt += wall - ls[r][c]
                ls[r][c] = wall  # 물 채워주기
print(cnt)
