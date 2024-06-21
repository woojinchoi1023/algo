# https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
ls = set()
for _ in range(N):
    ls.add(int(input()))

ls = list(ls)

dp = {}
for i in ls:
    dp[i]=1

for i in range(1,K+1):
    for j in ls:
        if dp.get(i-j,0):
            dp[i]=min(dp[i-j]+1,dp.get(i,1e9))

print(dp.get(K,-1))
