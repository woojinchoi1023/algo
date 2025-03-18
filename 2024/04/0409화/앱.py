# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

# N = 100?
# ls = [(apps[i], costs[i]) for i in range(N)]
# ls.sort(key=lambda x: x[1])
# print(ls)
dp = {0: 0}
# ans = float('inf')
for i in range(N):
    memory = apps[i]
    cost = costs[i]
    temp = {}
    for k, v in dp.items():
        temp[k+memory] = min(v+cost, dp.get(k+memory, float('inf')))
        # if k+memory >= M and ans > temp[k+memory]:
        #     ans = temp[k+memory]
    dp.update(temp)
    # print(dp)
print(dp)
# print(ans)
print(min([dp[i]for i in dp.keys() if i >= M]))
