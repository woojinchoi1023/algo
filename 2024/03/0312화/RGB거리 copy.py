# https://www.acmicpc.net/problem/1149
# import sys
# input = sys.stdin.readline
# 시간 초과


N = int(input().rstrip('\n'))
# ls = [list(map(int,input().split())) for _ in range(N)]
d = {}
for i in range(N):
    d[i] = list(map(int, input().rstrip('\n').split()))
cand = []


def dfs(idx, s, prev):
    if idx == N:
        cand.append(s)
        return
    temp = [0, 1, 2]
    for i in [j for j in temp if j != prev]:
        dfs(idx+1, s+d[idx][i], i)


dfs(0, 0, 3)
print(min(cand))
