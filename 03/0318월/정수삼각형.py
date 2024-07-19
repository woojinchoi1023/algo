# https://www.acmicpc.net/problem/1932

N = int(input())
ls = {}
for i in range(N):
    ls[i] = list(map(int, input().split()))

dp = {0: [ls[0][0]]}
for i in range(1, N):
    dp[i] = [0] * (i+1)
    dp[i][0] = dp[i-1][0]+ls[i][0]
    dp[i][-1] = dp[i-1][-1] + ls[i][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + ls[i][j]
# print(dp)
print(max(dp[N-1]))
