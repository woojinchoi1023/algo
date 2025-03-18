# https://www.acmicpc.net/problem/1916
from collections import deque
# import sys
# input = sys.stdin.readline
# 오답

N = int(input().rstrip('\n'))
d = {}
c = {}
for i in range(N):
    d[i+1] = []
    c[i+1] = [-1]*(N+1)
B = int(input().rstrip('\n'))
for _ in range(B):
    s, e, cost = map(int, input().rstrip('\n').split())
    d[s].append(e)
    if c[s][e] == -1:
        c[s][e] = cost
    else:
        c[s][e] = min(c[s][e], cost)
s, e = map(int, input().rstrip('\n').split())


def bfs(s, e):
    if s == e:
        return 0
    visited = [0]*(N+1)
    q = deque()
    q.append(s)
    v = set()
    while q:
        curr = q.popleft()
        # if curr == e:
        #     return visited[curr]
        for i in d[curr]:
            if i not in v or visited[i] > visited[curr] + c[curr][i]:
                visited[i] = visited[curr] + c[curr][i]
                v.add(i)
                q.append(i)
                # print(visited)
        # print(visited)
    return visited[e]


print(bfs(s, e))
