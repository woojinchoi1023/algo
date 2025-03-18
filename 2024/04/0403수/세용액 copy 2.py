# https://www.acmicpc.net/problem/2473
import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int,input().split()))
ls.sort()
best = float('inf')
ans = (0,0,0)
for i in range(N-2):
    fix = i
    start, end = i+1, N-1
    while start<end:
        s = ls[fix]+ls[start]+ls[end]
        if abs(s) < best:
            best = abs(s)
            ans = (ls[fix], ls[start], ls[end])
        if s>0:
            end-=1
        elif s<0:
            start+=1
        else:
            print(*ans)
            exit(0)

print(*ans)

