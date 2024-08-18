# https://www.acmicpc.net/problem/2842
from collections import deque

N = int(input())
ls = []
for i in range(N):
    ls.append(list(input()))
high = []
for i in range(N):
    high.append(list(map(int, input().split())))


cnt = 0

lower, upper = float('inf'), 0

all = set()

for i in range(N):
    for j in range(N):
        all.add(high[i][j])
        if ls[i][j] == 'P':
            sr, sc = i, j
            h = high[i][j]
            upper = max(upper, h)
            lower = min(lower, h)
        elif ls[i][j] == 'K':
            cnt += 1
            h = high[i][j]
            upper = max(upper, h)
            lower = min(lower, h)

d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

all = list(all)


def bfs(upper, lower):
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    dq = deque()
    dq.append((sr, sc))
    kcnt = 0  # k count
    while dq:
        r, c = dq.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if -1 < nr < N and -1 < nc < N and visited[nr][nc] == 0 and lower <= high[nr][nc] <= upper:
                visited[nr][nc] = 1
                dq.append((nr, nc))
                if ls[nr][nc] == 'K':
                    kcnt += 1
    if kcnt == cnt:
        return True
    else:
        return False


# print(upper, lower)
upperidx = all.index(upper)
# print(upperidx)
ans = 10e6
for i in all:
    if i > lower:
        break
    bot = upperidx
    top = len(all)-1
    while bot <= top:
        mid = (top+bot)//2
        res = bfs(all[mid], i)
        # print(i, all[mid], res)
        if res:
            ans = min(ans, all[mid]-i)
            top = mid-1
        else:
            bot = mid+1
# print(all)
print(ans)
