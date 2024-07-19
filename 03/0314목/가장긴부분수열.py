# https://www.acmicpc.net/problem/11053

N = int(input())
ls = list(map(int, input().split()))
dp = {0: 0}
seq = {0: 1}
for i in range(N):
    cand = [dp[j] for j in dp.keys() if j < ls[i]]
    dp[ls[i]] = max(cand)+1
    if i != 0:
        seq[i] = max(dp[ls[i]], seq[i-1])
# print(dp)
# print(seq)
print(seq[N-1])
