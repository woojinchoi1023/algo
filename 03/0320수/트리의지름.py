# https://www.acmicpc.net/problem/1967
# 틀렸습니다
# 4
# 1 2 1
# 2 3 3
# 4 2 2

N = int(input())
g = {}
for i in range(N-1):
    p, c, w = map(int, input().split())
    g.setdefault(p, [])
    g[p].append((c, w))
# print(g)
# print(p+1, N)  # leaf start
dp = {}
temp = {}  # for parent
for i in range(p+1, N+1):
    dp[i] = 0
    temp[i] = 0


def mxlen(root):
    if temp.get(root):
        return temp[root]
    child = g.get(root, [])
    mx = 0
    if child:
        mx = max([w+mxlen(c) for c, w in child])
    temp[root] = mx
    return temp[root]


mxlen(1)
print(temp)


# def sol(root):
#     if dp.get(root):
#         return dp[root]
#     child = g.get(root, [])
#     cnt = 0
#     for c, w in child:
#         cnt += temp[c]+w
#     dp[root] = cnt
#     return dp[root]

for i in range(N):
    child = g.get(i, [])
    cnt = 0
    for c, w in child:
        cnt += temp[c]+w
    dp[i] = cnt

print(dp)
print(max(dp.values()))
