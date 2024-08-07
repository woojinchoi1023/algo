# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ls = []
for _ in range(N):
    ls.append(int(input()))

dp = [0]*(K+1)
dp[0] = 1
for i in ls:  # 1 2 5
    for j in range(i, K+1):  # 2 3 4 5 6 7 8 9 10
        dp[j] += dp[j-i]
    print(dp)
print(dp[K])


'''
1: 1
2: 1+1,         2
3: 1+1+1,       2+1
4: 1+1+1+1,     2+1+1,     2+2
5: 1+1+1+1+1,   2+1+1+1,   2+2+1,          5
6: 1+1+1+1+1+1, 2+1+1+1+1, 2+2+1+1, 2+2+2, 5+1 

1+1+1+1+1+1, 2+1+1+1+1, 2+2+1+1, 5+1
1+1+1+1+2, 2+1+1+2, 2+2+2
1+1+1+3, 2+1+3

2,3인 경우
2: 2
3: 3
4: 2+2
5: 2+3
6: 2+2+2, 3+3 : 1*5=0 2*4=1 3*3=1
7: 2+2+3 : 1*6=0 2*5(1*4 2*3)=1 3*4(1*3 2*2)=1
서로소면 되는데

2,4인 경우
2:2
4:2+2, 4
6:2+2+2, 4+2
8:2+2+2+2, 4+2+2, 4+4


10 :
1,1,1,1,1,1,1,1,1,1
1,1,1,1,1,1,1,1,2
1,1,1,1,1,1,2,2
1,1,1,1,2,2,2
1,1,2,2,2,2
2,2,2,2,2


배수가 될 때 마다 커짐


1 2 3 4 5 6 7 8 9 10

'''
