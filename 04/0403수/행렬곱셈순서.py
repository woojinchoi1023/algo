# https://www.acmicpc.net/problem/11049
import sys
input= sys.stdin.readline
N = int(input())
ls = []
for _ in range(N):
    x,y = map(int,input().split())
    ls.append((x,y))

def matrix(arr1, arr2):
    # print('matrix')
    # print(arr1[0],arr1[1],arr2[1])
    return arr1[0] * arr1[1] * arr2[1]

print(ls)
m = N//2
i = m
j = m
curr = ls[m]
ans = 0
idx = 0
while idx<N-1:
    # left = (float('inf'), curr[0])
    # right = (curr[1], float('inf'))
    i-=1
    j+=1
    idx+=1
    print(i,m,j)
    if i==-1:
        m=j
        curr=(curr[0],ls[j][1])
        ans+=matrix(curr,ls[j])
    elif j==N:
        m=i
        curr=(ls[i][0],curr[1])
        ans+=matrix(ls[i], curr)
    elif matrix(ls[i], curr) > matrix(curr,ls[j]):
        # left = ls[i]
        # right= ls[j]
        m=j
        curr=(curr[0],ls[j][1])
        ans+=matrix(curr,ls[j])
    else:
        m=i
        curr=(ls[i][0],curr[1])
        ans+=matrix(ls[i], curr)
    print(ans)