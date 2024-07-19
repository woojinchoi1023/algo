# https://www.acmicpc.net/problem/12014


T = int(input())
for t in range(T):
    print(f'Case #{t+1}')
    N, K = map(int, input().split())
    ls = list(map(int, input().split()))
    ls = [0]+ls
    dp = [
        [0, 0, 0, 0]
    ]
    for i in range(1, N+1):
        idx = i-1
        while ls[idx] >= ls[i]:
            idx -= 1
        temp = [0, 0, 0, 0]
        temp[0] = dp[idx][0]+1
        temp[1] = ls[i]

        if dp[i-1][0] > dp[i-1][2]:
            temp[2] = dp[i-1][0]
            temp[3] = dp[i-1][1]
        elif dp[i-1][0] == dp[i-1][2]:
            temp[2] = dp[i-1][0]
            temp[3] = min(dp[i-1][1], dp[i-1][3])
        else:
            temp[2] = dp[i-1][2]
            temp[3] = dp[i-1][3]
        dp.append(temp)

    print(dp)
