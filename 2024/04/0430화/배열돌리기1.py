# https://www.acmicpc.net/problem/16926

import sys
from collections import deque

input=sys.stdin.readline

N,M,R = map(int,input().split())

ls = []
for _ in range(N):
    ls.append(list(map(int,input().split())))

height = N
width = M
weight = 0
outers= deque()
while height>0 and width>0:
    temp = deque()
    p=q=weight
    # print(ls[p][q], end=' ')
    temp.append(ls[p][q])
    for i in range(height-1):
        p+=1
        # print(ls[p][q], end=' ')
        temp.append(ls[p][q])
    for j in range(width-1):
        q+=1
        # print(ls[p][q], end=' ')
        temp.append(ls[p][q])
    for k in range(height-1):
        p-=1
        # print(ls[p][q], end=' ')
        temp.append(ls[p][q])
    for l in range(width-2):
        q-=1
        # print(ls[p][q], end=' ')
        temp.append(ls[p][q])
    height -= 2
    width -= 2
    weight += 1
    # print()
    # print(temp)
    temp.rotate(R)
    outers.append(temp)

# print(*outers,sep='\n')



ans = [[0]*M for _ in range(N)]
height = N
width = M
weight = 0
# while height>0 and width>0:
for _ in range(min(M,N)//2):
    curr = outers.popleft()
    p=q=weight
    ans[p][q]= curr.popleft()
    for i in range(height-1):
        p+=1
        ans[p][q]= curr.popleft()
    for j in range(width-1):
        q+=1
        ans[p][q]= curr.popleft()
    for k in range(height-1):
        p-=1
        ans[p][q]= curr.popleft()
    for l in range(width-2):
        q-=1
        ans[p][q]= curr.popleft()
    height -=2
    width -=2
    weight+=1

# print(*ans,sep='\n')
# print()
for i in ans:
    print(*i, sep=' ')



'''
4 4 2
1 12 11 10
2 13 16 9
3 14 15 8
4 5 6 7

3 4 1
1 2 3 4
5 6 7 8
9 10 11 12


input:
5 4 14
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28

answer:
1 2 3 4 
7 15 21 10 
13 9 20 16 
19 8 14 22 
25 26 27 28 

output:
1 2 3 4 
7 8 9 10 
13 14 15 16 
19 20 21 22 
25 26 27 28 

3 2 2
1 2
3 4
5 6

'''