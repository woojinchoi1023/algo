# https://www.acmicpc.net/problem/1113
import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
ls = []
for _ in range(N):
    ls.append(list(map(int, input().rstrip('\n'))))

# print(*ls, sep='\n')

d = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def bfs(r, c):


print()
