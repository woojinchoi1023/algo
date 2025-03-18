# https://www.acmicpc.net/problem/1937
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
ls = [list(map(int, input().split()))for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


dp = [[0]*N for _ in range(N)]


def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = 1
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if -1 < nr < N and -1 < nc < N and ls[r][c] < ls[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc)+1)
    return dp[r][c]


ans = 0
for r in range(N):
    for c in range(N):
        ans = max(dfs(r, c), ans)
print(ans)

'''
4
1 2 3 0
2 0 4 0
7 6 5 0
0 0 0 0


'''
