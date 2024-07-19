# https://www.acmicpc.net/problem/12014
# 시간초과


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    ls = list(map(int, input().split()))
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if ls[j] < ls[i]:
                dp[i] = max(dp[j]+1, dp[i])

    # print(dp)
    print(f'Case #{t+1}')
    for i in dp:
        if i >= K:
            print(1)
            break
    else:
        print(0)
