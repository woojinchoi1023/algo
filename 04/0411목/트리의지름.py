# https://www.acmicpc.net/problem/1167
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
g = {i: {}for i in range(N+1)}
in_arrows = [0]*(N+1)

for i in range(N):
    node, *data = map(int, input().split())
    for j in range((len(data)-1)//2):
        des, cost = data[j*2], data[j*2+1]
        g[node][des] = cost
        in_arrows[des] += 1

print(g)
print(in_arrows)

leaf = []
for i in range(1, N+1):
    if in_arrows[i] == 1:
        leaf.append(i)

for i in leaf:
    dp = [[]for _ in range(N+1)]
    dp[i].append(0)
    visited = [0]*(N+1)
    q = deque()
    q.append(i)
    while q:
        curr = q.popleft()
        visited[curr] = 1
        mx = max(dp[curr])
        for next, dist in g[curr].items():
            if not visited[next]:
                dp[next].append(mx+dist)
                q.append(next)
        print(dp)
    print()

'''
7
1 2 1 3 1 -1
2 1 1 4 1 5 1 -1
3 1 1 6 1 -1
4 2 1 7 1 -1
5 2 1 -1
6 3 1 -1
7 4 1 -1
'''
