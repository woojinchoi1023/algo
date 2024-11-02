# https://www.acmicpc.net/problem/1238
import heapq
N, M, X = map(int, input().split())
ls = [[float('inf')]*(N+1)for _ in range(N+1)]
rls = [[float('inf')]*(N+1)for _ in range(N+1)]  # reverse

for _ in range(M):
    s, e, t = map(int, input().split())
    ls[s][e] = t
    rls[e][s] = t

'''
[inf, inf, inf, inf, inf]
[inf, inf,   4,   2,   7]
[inf,   1, inf,   5, inf]
[inf,   2, inf, inf,   4]
[inf, inf,   3, inf, inf]
'''
# print(*ls, sep='\n')


def dijk(start, ls):
    dist = [float('inf')for _ in range(N+1)]
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        d, curr = heapq.heappop(hq)
        if d > dist[curr]:
            continue
        for i in range(1, N+1):
            if i == curr:
                continue
            if dist[i] > ls[curr][i]+d:
                dist[i] = ls[curr][i]+d
                heapq.heappush(hq, (ls[curr][i]+d, i))

    return dist


# X -> i
a = dijk(X, ls)
# i -> X
b = dijk(X, rls)

ans = 0
for i in range(1, N+1):
    if i == X:
        continue
    ans = max(ans, a[i]+b[i])

print(ans)
