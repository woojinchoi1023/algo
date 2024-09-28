# https://www.acmicpc.net/problem/1520

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


R, C = map(int, input().split())

ls = [list(map(int, input().split()))for _ in range(R)]
dp = [[-1]*C for _ in range(R)]  # 답이 아닌 경로는 다시 검사하는 걸 막아야 함
dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# memo
dp[R-1][C-1] = 1


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for dr, dc in dt:
        nr, nc = r+dr, c+dc
        if -1 < nr < R and -1 < nc < C and ls[nr][nc] < ls[r][c]:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]


dfs(0, 0)
# print(*dp, sep='\n')
print(dp[0][0])

''' 
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
[3, 2, 2, 2, 1]
[1, 0, 0, 1, 1]
[1, 0, 0, 1, 0]
[1, 1, 1, 1, 1]

'''
