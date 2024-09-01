# https://www.acmicpc.net/problem/2842
from collections import deque

N = int(input())

ls = [list(input()) for _ in range(N)]

high = [list(map(int, input().split())) for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

sr, sc = 0, 0  # start r, c
k = 0

highs = set()
for i in range(N):
    for j in range(N):
        highs.add(high[i][j])
        if ls[i][j] == 'K':
            k += 1
        elif ls[i][j] == 'P':
            sr, sc = i, j

highs = list(highs)
highs.sort()


def bfs(r, c, top, bot):
    dq = deque()
    dq.append((r, c))
    v = [[0]*N for _ in range(N)]
    v[r][c] = 1
    cnt = 0
    while dq:
        r, c = dq.popleft()
        if ls[r][c] == 'K':
            cnt += 1
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < N and v[nr][nc] == 0 and bot <= high[nr][nc] <= top:
                v[nr][nc] = 1
                dq.append((nr, nc))

    return True if cnt == k else False


# print(highs)
ans = 10e9
lh = len(highs)
for i in range(lh):
    j = lh-1
    bot = highs[i]
    if high[sr][sc] < bot:
        continue
    while i <= j:
        m = (i+j)//2
        top = highs[m]
        # print(bot, top)

        if bfs(sr, sc, top, bot):
            ans = min(ans, top-bot)
            j = m-1
        else:
            i = m+1

print(ans)
