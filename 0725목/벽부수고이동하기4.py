# https://www.acmicpc.net/problem/16946

a, b = map(int, input().split())

ls = [list(map(int, input())) for _ in range(a)]

# print(*ls, sep='\n')
dp = [[-1]*b for _ in range(a)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    if ls[r][c] == 0:
        return
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if -1 < nr < a and -1 < nc < b and ls[nr][nc] == 0:
            dp[r][c] += dfs(nr, nc)+1
    # dp[r][c]
    return dp[r][c]


for i in range(a):
    for j in range(b):
        if ls[i][j] == 1:
            dfs(i, j)
            dp[i][j] += 1
            print(*dp, sep='\n')
            print()
