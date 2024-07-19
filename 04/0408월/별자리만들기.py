# https://www.acmicpc.net/problem/4386

import heapq
import sys
input = sys.stdin.readline

N = int(input())
visited = {}
for _ in range(N):
    x, y = map(float, input().split())
    visited[(x, y)] = 0

cnt = 0
ans = 0
hq = []
heapq.heappush(hq, [0, (x, y)])
while hq:
    w, curr = heapq.heappop(hq)
    if visited[curr]:
        continue
    # print(curr, hq)
    ans += w
    visited[curr] = 1
    x, y = curr
    for next in visited.keys():
        if visited[next]:
            continue
        nextx, nexty = next
        heapq.heappush(
            hq, [((nextx-x)**2 + (nexty-y)**2)**(1/2), (nextx, nexty)])
print(ans)
