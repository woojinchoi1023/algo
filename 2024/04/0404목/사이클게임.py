# https://www.acmicpc.net/problem/20040
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
p = [i for i in range(N)]

def parent(x):
    if p[x] != x:
        p[x]=parent(p[x])
    return p[x]

def union(x,y):
    if parent(x)>parent(y):
        p[parent(y)]=parent(x)
    else:
        p[parent(x)]=parent(y)


for i in range(M):
    x,y = map(int,input().split())
    if parent(x)==parent(y):
        print(i+1)
        break
    union(x,y)
else:
    print(0)