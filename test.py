# https://www.acmicpc.net/problem/1167


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

V = int(input())
g = {i: {} for i in range(1, V+1)}

for i in range(V):
    a, *ls, _ = map(int, input().split())
    for j in range(0, len(ls), 2):
        g[a][ls[j]] = ls[j+1]

# print(g)

'''
{1: {3: 2}, 2: {4: 4}, 3: {1: 2, 4: 3}, 4: {2: 4, 3: 3, 5: 6}, 5: {4: 6}}
'''

# 트리의 지름: 임의의 한점 -> 가장 먼 점 -> 가장 먼 점
mx = 0
mx_idx = 0
visited = [0]*(V+1)


def dfs(node, res):
    global mx, mx_idx
    visited[node] = 1
    if res > mx:
        mx = res
        mx_idx = node
    for child in g.get(node, []):
        if not visited[child]:
            visited[child] = 1
            dfs(child, res+g[node][child])
            visited[child] = 0


dfs(1, 0)

mx = 0
visited = [0]*(V+1)
dfs(mx_idx, 0)

print(mx)
