# https://www.acmicpc.net/problem/11724

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip('\n').split())
ls = [[]for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().rstrip('\n').split())
    ls[a].append(b)
    ls[b].append(a)

visited = [0]*(N+1)


def bfs(s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        if visited[s] == 0:
            visited[s] = 1
            q.extend(ls[s])


cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)
