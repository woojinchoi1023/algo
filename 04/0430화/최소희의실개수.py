# https://www.acmicpc.net/problem/19598

import sys, heapq
input= sys.stdin.readline   

N = int(input())
ls = []
for _ in range(N):
    ls.append(list(map(int,input().split())))
ls.sort()
# print(ls)

hq = [ls[0][1]]

for i in range(1,N):
    s,e = ls[i]
    if hq[0] > s:
        heapq.heappush(hq,e)
    else:
        heapq.heappop(hq)
        heapq.heappush(hq,e)

print(len(hq))
'''
6
1 2
1 3
2 3
3 4
3 5
2 5
'''