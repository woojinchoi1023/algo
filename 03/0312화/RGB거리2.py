# https://www.acmicpc.net/problem/1149
# import sys
# input = sys.stdin.readline
import copy

N = int(input().rstrip('\n'))
temp = {}
for i in range(N):
    temp[i] = list(map(int, input().rstrip('\n').split()))


ans = []
for k in range(3):
    d = copy.deepcopy(temp)
    dp = {
        0: d[0],
    }

    d[0][k-1] = d[0][k-2] = float('inf')

    for i in range(1, N):
        dp[i] = [0]*3
        for j in range(3):
            dp[i][j] = d[i][j] + min(dp[i-1][j-1], dp[i-1][j-2])

    # print(dp)
    ans.append(min(dp[N-1][k-1], dp[N-1][k-2]))
    # print(min(dp[N-1][k-1], dp[N-1][k-2]))

print(min(ans))
