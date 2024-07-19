# https://www.acmicpc.net/problem/1647

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N,M = map(int,input().split())

hq = []
for _ in range(M):
    x,y,z = map(int,input().split())
    heappush(hq,(z,(x,y)))
p = [i for i in range(N+1)]
def parent(c):
    if p[c]!=c:
        p[c]=parent(p[c])
    return p[c]

def union(a,b):
    if parent(a)>parent(b):
        p[parent(a)]=parent(b)
    else:
        p[parent(b)]=parent(a)

ans=0
# print(hq)
idx =0
while idx<N-2:
    z,curr = heappop(hq)
    x,y = curr
    if parent(x)==parent(y):
        continue
    union(x,y)
    ans+=z
    # print(p)
    idx+=1
print(ans)

