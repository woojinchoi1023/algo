# https://www.acmicpc.net/problem/1697
N, K = map(int, input().split())
dp = {
    N: 0,
    N+1: 1,
    N-1: 1,
}
if N:
    dp[N*2] = 1
# print(dp)

if N >= K:
    print(N-K)
else:
    for i in range(N+1, K+1):
        # if dp.get(i):
        #     if dp[i] > dp[i-1]+1:
        #         dp[i] = dp[i-1]+1
        #     continue
        temp = [i-1, i+1, i/2]
        cand = [dp[j] for j in temp if dp.get(j, -1) != -1]
        if dp.get(i):
            dp[i] = min(min(cand) + 1, dp[i])
        else:
            dp[i] = min(cand) + 1
        if dp.get(i*2):
            dp[i*2] = min(dp[i*2], dp[i] + 1)
        else:
            dp[i*2] = dp[i] + 1

    print(dp[K])
    # print(dp)


# checked = [0]*(K+1)


# def t(N):
#     cand = []
#     cand.append(N-1)
#     cand.append(N+1)
#     if not N % 2:
#         cand.append(N//2)
#     temp = []
#     for i in cand:
#         if not dp.get(i) and checked[i] == 0:
#             checked[i] = 1
#             t(i)
#         elif checked[i] == 1 and not dp.get(i):
#         else:
#             checked[i] = 1
#         temp.append(dp[i])

#     dp[N] = min(temp)+1


# t(K)
# print(dp[K])
# print(dp)
