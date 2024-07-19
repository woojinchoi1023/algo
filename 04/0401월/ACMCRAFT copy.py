# https://www.acmicpc.net/problem/1005
from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for t in range(T):
    N, K = map(int, input().rstrip().split())
    ls = [0] + list(map(int, input().rstrip().split()))
    g = {
        i: {}for i in range(N+1)
    }
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        g[y][x] = ls[x]

    print(g)

    W = int(input().rstrip())


def djik(s):
    dist = [float('inf')]*(N+1)
    dist[s] = ls[s]
