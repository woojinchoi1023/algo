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
    dist_run[start] = 0
    dist_walk[start] = 0

    hq = []
    heapq.heappush(hq, (0, start, True))
    while hq:
        print(hq)
        d, node, run = heapq.heappop(hq)
        # print(d, node, run)
        # print(dist_run)
        # print(dist_walk)
        print()
        if run:
            if d > dist_run[node]:
                continue
            for child in g[node].keys():
                child_dist = g[node][child]
                child_dist /= 2
                if d+child_dist < dist_run[child]:
                    dist_run[child] = d+child_dist
                    heapq.heappush(hq, (d+child_dist, child, not run))
        else:
            if d > dist_walk[node]:
                continue
            for child in g[node].keys():
                child_dist = g[node][child]
                child_dist *= 2
                if d+child_dist < dist_walk[child]:
                    dist_walk[child] = d+child_dist
                    heapq.heappush(hq, (d+child_dist, child, not run))
    return dist_run, dist_walk

    #     if d > dist[node]:
    #         continue
    #     if run:
    #         new_run = False
    #     else:
    #         new_run = True
    #     for child in g[node].keys():
    #         child_dist = g[node][child]
    #         if run:
    #             child_dist /= 2
    #         else:
    #             child_dist *= 2
    #         if d + child_dist <= dist[child]:
    #             dist[child] = d + child_dist
    #             heapq.heappush(hq, (d+child_dist, child, new_run))
    # return dist


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
print(res[0])
print()
print(res[1])

# foxRes = fox(1)
# print()
# print(foxRes)
