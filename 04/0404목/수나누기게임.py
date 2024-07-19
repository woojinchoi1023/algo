# https://www.acmicpc.net/problem/27172

import sys
input = sys.stdin.readline

# N = 100000

N = int(input())
ls = list(map(int,input().split()))

#      3  4 12
#  3  p1  d  w  +1 
#  4   d p2  w  +1
# 12   l  l p3  -2
# s =[0]*(N)
# for i in range(N):
#     for j in range(i,N):
#         if ls[j]%ls[i] == 0:
#             s[i]+=1
#             s[j]-=1
#         elif ls[i]%ls[j]==0:
#             s[i]-=1
#             s[j]+=1
# print(s)
mx = max(ls)
score = [0]*(mx+1)
for i in range(N):
    k = ls[i]
    for j in range(k*2, mx+1, k):
        score[k]+=1
        score[j]-=1
print(score)
for i in ls:
    print(score[i],end=' ')

            