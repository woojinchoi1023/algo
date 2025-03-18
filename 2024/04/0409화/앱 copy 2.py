# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

# N = 100?
ls = [(apps[i], costs[i]) for i in range(N)]
ls.sort(key=lambda x: (x[1], -x[0]))
sorted_apps = [i[0] for i in ls]
sorted_costs = [i[1] for i in ls]
# print(ls)
print(sorted_apps)
print(sorted_costs)
# [(10, 0), (30, 3), (20, 3), (40, 4), (35, 5)]
# [10, 30, 20, 40, 35]
# [0, 3, 3, 4, 5]
i, j = 0, N-1
cost = sum(sorted_costs[i:j+1])
while i <= j:
    memory = sum(sorted_apps[i:j+1])
    # print(i, j, memory)
    if memory-sorted_apps[j] >= M:
        j -= 1
    elif memory-sorted_apps[i] >= M:
        i += 1
    else:
        print(sum(sorted_costs[i:j+1]))
        break
