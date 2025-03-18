# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

# N = 100?
ls = [(apps[i], costs[i]) for i in range(N)]
ls.sort(key=lambda x: (x[1], -x[0]))
print(ls)
dp = {0: 0}
# ans = float('inf')
for i in range(N):
    memory = ls[i][0]
    cost = ls[i][1]
    temp = {}
    for k, v in dp.items():
        temp[k+memory] = min(v+cost, dp.get(k+memory, float('inf')))
        if k+memory >= M:
            print(temp[k+memory])
            exit()
    dp.update(temp)
    # print(dp)
