# https://www.acmicpc.net/problem/1967
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input().rstrip('\n'))
g = {}
parents = []
for i in range(N-1):
    p, c, w = map(int, input().rstrip('\n').split())
    g.setdefault(p, [])
    g[p].append((c, w))
    if p not in parents:
        parents.append(p)

# memorization
# 부모 노드 별 자식들의 최대값을 저장
dp = {}


def sol(root, s):
    if dp.get(root):
        return dp[root]
    child = g.get(root, [])
    if not child:
        dp[root] = [0]
        return [s]
    cand = []
    for c, w in child:
        cand.append(max(sol(c, s))+w)
    if not dp.get(root):
        dp[root] = cand
    return cand


mx = 0
for i in parents:
    t = sorted(sol(i, 0))
    if sum(t[-2:]) > mx:
        mx = sum(t[-2:])

print(mx)
