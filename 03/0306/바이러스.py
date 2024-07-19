# https://www.acmicpc.net/problem/2606
from collections import deque
N = int(input())
ls = [[]for i in range(N+1)]
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)
cnt = 0
q = deque()
q.append(1)
visited = [0]*(N+1)
while q:
    curr = q.popleft()
    if not visited[curr]:
        q.extend(ls[curr])
        if curr != 1:
            cnt += 1
    visited[curr] = 1
print(cnt)
