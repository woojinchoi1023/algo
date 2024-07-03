# https://www.acmicpc.net/problem/4991

import heapq
import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        exit()
    ls = [list(input().rstrip('\n')) for _ in range(N)]
    # print(*ls, sep='\n')
    tar = []
    for r in range(N):
        for c in range(M):
            if ls[r][c] == '*':
                tar.append((r, c))
            elif ls[r][c] == 'o':
                tar.append((r, c))
                start = (r, c)
            # elif ls[r][c] == 'o':
            #     start = (r, c)
    # tar.append((r, c))
    # print(tar)

    def dijk(r, c):
        dist = [[float('inf')]*M for _ in range(N)]
        dist[r][c] = 0
        hq = []
        heapq.heappush(hq, (0, r, c))
        while hq:
            d, r, c = heapq.heappop(hq)
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                if -1 < nr < N and -1 < nc < M and ls[nr][nc] != 'x' and dist[nr][nc] > d+1:
                    dist[nr][nc] = d+1
                    heapq.heappush(hq, (d+1, nr, nc))
        # print(*dist, sep='\n')
        return dist
    data = {}
    # edge = []
    for r, c in tar:
        dist = dijk(r, c)
        for row, col in tar:
            if (r, c) == (row, col):
                continue
            # heapq.heappush(edge, (dist[row][col], (r, c), (row, col)))
            data[((r, c), (row, col))] = dist[row][col]

    # print(data)

    visited = {
        i: 0 for i in tar
    }
    visited[start] = 1
    # visited[start]=1
    ans = float('inf')

    def dfs(r, c, res, depth):
        global ans
        if depth == len(tar):
            ans = min(ans, res)
            return

        for nr, nc in tar:
            if visited[(nr, nc)] == 0:
                visited[(nr, nc)] = 1
                dfs(nr, nc, res+data[((r, c), (nr, nc))], depth+1)
                visited[(nr, nc)] = 0

    dfs(start[0], start[1], 0, 1)
    # print(ans)

    if ans == float('inf'):
        ans = -1
    print(ans)
