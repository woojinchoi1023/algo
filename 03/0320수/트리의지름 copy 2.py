# https://www.acmicpc.net/problem/1967

N = int(input())
g = {}
parents = []
for i in range(N-1):
    p, c, w = map(int, input().split())
    g.setdefault(p, [])
    g[p].append((c, w))
    parents.append(p)


def sol(root, s):
    child = g.get(root, [])
    if not child:
        return [s]
    cand = []
    for c, w in child:
        cand.append(max(sol(c, s+w)))
    return cand


mx = 0
for i in parents:
    t = sorted(sol(i, 0))
    if sum(t[-2:]) > mx:
        mx = sum(t[-2:])

print(mx)
# print(i)
# print(sol(i, 0))
