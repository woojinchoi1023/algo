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
all = set()
house = set()

for i in range(N):
    for j in range(N):
        all.add(high[i][j])
        if ls[i][j] == 'P':
            sr, sc = i, j
            h = high[i][j]
            house.add(h)
        elif ls[i][j] == 'K':
            cnt += 1
            h = high[i][j]
            house.add(h)


all = list(all)
all.sort()  # 없으면 틀림

minH, maxH = min(house), max(house)

d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


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


upperidx = all.index(maxH)
ans = 10e6
for i in all:
    if i > minH:
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
print(ans)


'''
4
.K.K
K..K
P..K
K...
889065 410637 837320 399872
531498 929923 153678 295021
340357 352205 77487 574205
346047 227896 804677 961686

420527

'''
