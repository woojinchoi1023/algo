# https://www.acmicpc.net/problem/1927
import heapq
import sys
input = sys.stdin.readline
ls = []
n = int(input().rstrip('\n'))
for i in range(n):
    s = int(input().rstrip('\n'))
    if s:
        heapq.heappush(ls, s)
    else:
        if ls:
            print(heapq.heappop(ls))
        else:
            print(0)
