# https://www.acmicpc.net/problem/1697
from collections import deque
N, K = map(int, input().split())
d = {N: 0}


def bfs(s):
    global K
    q = deque()
    q.append(s)
    while q:
        curr = q.popleft()
        if curr > 2*K or curr < 0:
            continue

        for i in [curr-1, curr+1, curr*2]:
            if d.get(i, -1) != -1:
                continue
            d[i] = d[curr]+1
            q.append(i)


if N > K:
    print(N-K)
else:
    bfs(N)
    # print(d)
    print(d[K])
# print(d)
# 5 10 9 18 17
