# https://www.acmicpc.net/problem/2533
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
g = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


dp = {}


def dfs(node, v):
    if dp.get(node):
        return dp[node]
    v[node] = 1
    # 내가 얼리인 경우 : 자식들 최소 합 + 1
    yes = 1
    # 내가 얼리가 아닌 경우 : 자식들 yes 합
    no = 0
    for c in [i for i in g.get(node) if v[i] == 0]:
        yes += min(dfs(c, v))
        no += dfs(c, v)[0]
    dp[node] = [yes, no]
    return dp[node]


dfs(1, [0]*(N+1))
# print(dp)
print(min(dp[1]))
