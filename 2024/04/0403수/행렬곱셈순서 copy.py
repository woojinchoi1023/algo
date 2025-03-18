# https://www.acmicpc.net/problem/11049
'''
반례
4
5 3
3 2
2 6
6 3

'''
import sys
input= sys.stdin.readline
N = int(input())
ls = []
for _ in range(N):
    x,y = map(int,input().split())
    ls.append((x,y))

def matrix(arr1, arr2):
    return arr1[0] * arr1[1] * arr2[1]

# print(ls)
i = N//2-1
j = N//2+1
curr = ls[N//2]
ans = 0
while i>-1 or j<N:
    print(i,curr,j)
    left=(float('inf'),float('inf'))
    right=(float('inf'),float('inf'))
    if i>-1:
        left=ls[i]
    if j<N:
        right=ls[j]
    if matrix(left, curr) > matrix(curr,right): # right
        j+=1
        ans+=matrix(curr,right)
        curr=(curr[0],right[1])
    else: # left
        i-=1
        ans+=matrix(left, curr)
        curr=(left[0],curr[1])

print(ans)