# https://www.acmicpc.net/problem/27172

import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int,input().split()))
d = {
    v:i for i,v in enumerate(ls)
}

mx = max(ls)
score = [0]*(N)
for i in range(N):
    k = ls[i]
    for j in range(k*2,mx+1,k):
        if j in d:
            score[i]+=1
            score[d[j]]-=1

            
print(*score)


