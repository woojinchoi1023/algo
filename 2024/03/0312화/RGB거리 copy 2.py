# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
d = {}
for i in range(N):
    d[i] = list(map(int, input().rstrip('\n').split()))

dp = {
    0: d[0],
}

for i in range(1, N):
    dp[i] = [0]*3
    for j in range(3):
        dp[i][j] = d[i][j] + min(dp[i-1][j-1], dp[i-1][j-2])

print(min(dp[N-1]))
