# https://www.acmicpc.net/problem/2842
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


N = int(input())

ls = [list(input()) for _ in range(N)]

high = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

top, bot = 0, 10e9
for i in range(N):
    for j in range(N):
        curr = high[i][j]
        if ls[i][j] == 'P':
            sr, sc = i, j
            top = max(top, curr)
            bot = min(bot, curr)
        elif ls[i][j] == 'K':
            top = max(top, curr)
            bot = min(bot, curr)

print(top, bot)

hq = []

# heapq.heappush(hq, (0, ls[sr][sc],ls[sr][sc], sr,sc, set() )) # cost, top, bot, r, c

# while hq:
#     r,c = heapq.heappop(hq)
