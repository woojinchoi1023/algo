# https://www.acmicpc.net/problem/2252
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().rstrip('\n').split())
g = [[]for _ in range(N+1)]
in_arrow = [0]*(N+1)
for _ in range(M):
    x,y = map(int,input().rstrip('\n').split())
    g[x].append(y)
    in_arrow[y]+=1
# 위상정렬
dq = deque()
for i in range(1,N+1):
    if in_arrow[i]==0:
        dq.append(i)
        print(i,end=' ')
while dq:
    curr = dq.popleft()
    for nxt in g[curr]:
        in_arrow[nxt] -= 1
        if in_arrow[nxt] == 0:
            dq.append(nxt)
            print(nxt, end=' ')

