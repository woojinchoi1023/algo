# https://www.acmicpc.net/problem/15681
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

g = {i: [] for i in range(1, N+1)}

for i in range(N-1):
    U, V = map(int, input().split())
    g[U].append(V)
    g[V].append(U)
q = [int(input()) for _ in range(Q)]

visited = [0]*(N+1)
ans = [1]*(N+1)


def dfs(root):
    for c in g.get(root):
        if not visited[c]:
            visited[c] = 1
            dfs(c)
            ans[root] += ans[c]


visited[R] = 1
dfs(R)

for i in q:
    print(ans[i])
