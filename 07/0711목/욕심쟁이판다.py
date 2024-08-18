# https://www.acmicpc.net/problem/1937
# 하나금융TI 기출 3번
from collections import deque

N = int(input())
ls = [list(map(int, input().split()))for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

visited = [[0]*N for _ in range(N)]


def bfs(r, c):
    global N, ans
    dq = deque()
    dq.append((r, c))
    visited[r][c] = 1
    while dq:
        r, c = dq.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < N and ls[nr][nc] > ls[r][c]:
                visited[nr][nc] = visited[r][c] + 1
                ans = max(ans, visited[nr][nc])
                dq.append((nr, nc))
    # print(*visited, sep='\n')
    # print()


for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs(r, c)
print(ans)

'''
4
1 2 3 0
2 0 4 0
7 6 5 0
0 0 0 0


'''
