# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline
# 43퍼에서 시간초과


N = int(input().rstrip('\n'))
d = {}
for i in range(N):
    d[i] = list(map(int, input().rstrip('\n').split()))

ans = 0

p = 3
for i in range(N):
    c = [[j, d[i][j]] for j in [0, 1, 2] if j != p]
    c.sort(key=lambda x: x[1])
    p = c[0][0]
    ans += c[0][1]

# print('greedy:', ans)


def dfs(idx, s, prev):
    global ans
    if ans <= s:
        return
    if idx == N:
        if ans > s:
            ans = s
        return
    temp = [0, 1, 2]

    for i in [j for j in temp if j != prev]:
        dfs(idx+1, s+d[idx][i], i)


dfs(0, 0, 3)
print(ans)
