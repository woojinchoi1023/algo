# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))


dp = {0: 0}  # cost:max(memory)
for i in range(N):
    memory = apps[i]
    cost = costs[i]
    temp = {}
    for k, v in dp.items():
        temp[k+cost] = max(v+memory, dp.get(k+cost, 0), temp.get(k+cost, 0))

    dp.update(temp)
    # print(dp)

c = 0
while True:
    if dp.get(c, 0) >= M:
        print(c)
        exit()
    c += 1

# print(ans)
# print(min([dp[i]for i in dp.keys() if i >= M]))
