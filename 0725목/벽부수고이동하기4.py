# https://www.acmicpc.net/problem/16946
from collections import deque

a, b = map(int, input().split())

ls = [list(map(int, input())) for _ in range(a)]

v = [[0]*b for _ in range(a)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

'''
4 5
11001
00111
01010
10101

[0, 0, 1, 1, 0]
[2, 2, 0, 0, 0]
[2, 0, 3, 0, 4]
[0, 5, 0, 6, 0]

3 3
101
111
101

1 1
0
'''

area = {}


def bfs(r, c, idx):
    # visited = [[0]*b for _ in range(a)]
    # visited[r][c] = 1
    v[r][c] = idx
    dq = deque()
    dq.append((r, c))
    area[idx] += 1
    while dq:
        r, c = dq.popleft()
        for dr, dc in d:
            nr, nc = dr+r, dc+c
            if -1 < nr < a and -1 < nc < b and ls[nr][nc] == 0 and v[nr][nc] == 0:
                # visited[nr][nc] = 1
                v[nr][nc] = idx
                dq.append((nr, nc))
                area[idx] += 1


idx = 1
for i in range(a):
    for j in range(b):
        if v[i][j] == 0 and ls[i][j] == 0:
            area[idx] = 0
            bfs(i, j, idx)
            idx += 1
            # print(*v, sep='\n')
            # print()
# print(area)

ans = [[0]*b for _ in range(a)]

for i in range(a):
    for j in range(b):
        if ls[i][j] == 1:
            mem = set()
            for dr, dc in d:
                nr, nc = i+dr, j+dc
                if -1 < nr < a and -1 < nc < b and ls[nr][nc] == 0:
                    mem.add(v[nr][nc])
            ans[i][j] += 1
            for areaidx in mem:
                ans[i][j] += area[areaidx]
# print(*ans, sep='\n')
for k in ans:
    # print(k)
    print(''.join(map(str, k)))
