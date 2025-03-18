# https://www.acmicpc.net/problem/2623

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

ls = []
g = [[]for _ in range(N+1)]
in_arrows = [0]*(N+1)
for _ in range(M):
    num, *l = map(int, input().split())
    for i in range(1, num):
        g[l[i-1]].append(l[i])
        in_arrows[l[i]] += 1
    # ls.append(l)

# print(g)
# print(in_arrows)
# [[], [4], [5, 3], [], [3], [4], [2]]
# [0, 0, 1, 2, 2, 1, 0]
# 위상정렬
dq = deque()
for i in range(1, N+1):
    if in_arrows[i] == 0:
        dq.append(i)
ans = []
while dq:
    curr = dq.popleft()
    ans.append(curr)
    for i in g[curr]:
        in_arrows[i] -= 1
        if in_arrows[i] == 0:
            dq.append(i)

if len(ans) == N:
    print(*ans, sep='\n')
else:
    print(0)
