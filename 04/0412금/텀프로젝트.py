# https://www.acmicpc.net/problem/9466
from collections import deque
T = int(input())
for t in range(T):
    N = int(input())
    g = [0]*(N+1)
    ls = list(map(int, input().split()))
    for i in range(N):
        g[i+1] = ls[i]
    print(g)
