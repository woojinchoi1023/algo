# https://www.acmicpc.net/problem/3430
import heapq
Z = int(input())
for _ in range(Z):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    lake = [True]*(N+1)
    g = [[] for _ in range(N + 1)]
    for i in range(M-1, -1, -1):
        if ls[i]:
            g[ls[i]].append(i)
    q = []
    for lakeIdx in range(1, N+1):
        if not g[lakeIdx]:
            continue
        day = g[lakeIdx].pop()
        heapq.heappush(q, (day, lakeIdx))
    ans = []
    can = True
    for i in range(M):
        num = ls[i]
        if num == 0:
            if q:  # drink
                day, lakeIdx = heapq.heappop(q)
                lake[lakeIdx] = False
                ans.append(lakeIdx)
            else:  # nothing to drink
                ans.append(0)
        else:
            if lake[num]:  # already full
                can = False
                break
            lake[num] = True
            if g[num]:
                heapq.heappush(q, (g[num].pop(), num))
    if can:
        print('YES')
        print(' '.join(map(str, ans)))
    else:
        print('NO')
