# https://www.acmicpc.net/problem/16118
import heapq
N, M = map(int, input().split())
g = {i: {} for i in range(1, N+1)}
for _ in range(M):
    a, b, d = map(int, input().split())
    g[a][b] = d
    g[b][a] = d

# print(g)


def wolf(start):
    dist_run = [float('inf') for _ in range(N+1)]
    dist_walk = [float('inf') for _ in range(N+1)]
    dist_run[start] = 0  # 이러면 반례 있음
    dist_walk[start] = 0

    hq = []
    heapq.heappush(hq, (0, start, True))
    while hq:
        # print(hq)
        d, node, run = heapq.heappop(hq)
        # print(d, node, run)
        # print(dist_run)
        # print(dist_walk)
        # print()
        if run:
            if d > dist_walk[node]:
                continue
            for child in g[node].keys():
                child_dist = g[node][child]
                child_dist /= 2
                if d+child_dist < dist_run[child]:
                    dist_run[child] = d+child_dist
                    heapq.heappush(hq, (d+child_dist, child, not run))
        else:
            if d > dist_run[node]:
                continue
            for child in g[node].keys():
                child_dist = g[node][child]
                child_dist *= 2
                if d+child_dist < dist_walk[child]:
                    dist_walk[child] = d+child_dist
                    heapq.heappush(hq, (d+child_dist, child, not run))
    return dist_run, dist_walk


def fox(start):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        d, node = heapq.heappop(hq)
        if d > dist[node]:
            continue
        for child in g[node].keys():
            child_dist = g[node][child]
            if d+child_dist < dist[child]:
                dist[child] = d+child_dist
                heapq.heappush(hq, (d+child_dist, child))
    return dist


res = wolf(1)
# print(res[0])
# print()
# print(res[1])

foxRes = fox(1)
# print()
# print(foxRes)

cnt = 0
for i in range(2, N+1):
    if foxRes[i] < res[0][i] and foxRes[i] < res[1][i]:
        cnt += 1
print(cnt)

'''
5 5
1 2 1
1 4 5
1 5 3
4 5 4
2 3 400

[inf, 12.0, 0.5, 214.0, 2.5, 1.5]

[inf, 0, 14.0, 800.5, 9.5, 10.5]

[inf, 0, 1, 401, 5, 3]


[inf, 0, 0.5, inf, 2.5, 1.5]

[inf, 0, inf, 800.5, 9.5, 10.5]

[inf, 0, 1, 401, 5, 3]

'''
