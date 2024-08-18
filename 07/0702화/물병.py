# https://www.acmicpc.net/problem/1052
# 시간초과
N, M = map(int, input().split())

g = {i: 0 for i in range(25)}


g[0] = N
# print(g)
ans = 0
while sum(g.values()) > M:
    change = False
    for i in range(24):
        if g[i] >= 2:
            g[i+1] += g[i]//2
            g[i] %= 2
            change = True
    if not change:
        g[0] += 1
        ans += 1
    # print(g)
print(ans)
