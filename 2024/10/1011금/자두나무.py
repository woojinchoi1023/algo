# https://www.acmicpc.net/problem/2240
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
ls = [int(input())for _ in range(T)]

dp = [[0]*(W+1) for _ in range(T)]
if ls[0] == 1:
    dp[0][0] = 1
    dp[0][1] = 0
else:
    dp[0][0] = 0
    dp[0][1] = 1

for i in range(1, T):
    for j in range(min(i+1, W+1)):
        same = 0
        if j % 2 == 0 and ls[i] == 1:
            same = 1
        elif j % 2 == 1 and ls[i] == 2:
            same = 1

        if j > 0:  # shift
            dp[i][j] = max(dp[i-1][j]+same, dp[i-1][j-1]+same)
        else:  # no
            dp[i][j] = dp[i-1][j]+same


print(max(dp[T-1]))
'''
홀수 움직였다 : 2
0또는 짝수    : 1

  j 0 1 2 3 4 5 6 7 (=움직인수)
i
0   1 1
1   . . .
2   . . . .
3
4
5
6
7
8
9
(=i번째 수)
'''
