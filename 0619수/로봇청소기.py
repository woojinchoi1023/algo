# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
r,c,d = map(int,input().split())
'''
  0
3   1
  4
'''
ls = []
for _ in range(N):
    ls.append(list(map(int,input().split())))

dq = deque([
    (0,-1), # 왼
    (1,0),  # 밑
    (0,1),  # 오
    (-1,0), # 위
])

dq.rotate(d)

cnt = 0

while True:
    if ls[r][c] == 0: # 현재 청소 안되어있으면 청소
        cnt+=1
        ls[r][c]=-1

    rot = 0 # 반시계 90도 회전

    for dr,dc in dq:
        rot-=1
        if -1<r+dr<N and -1<c+dc<M and ls[r+dr][c+dc] == 0:
            r+=dr
            c+=dc
            dq.rotate(rot)
            break
    else: # 후진
        if -1<r-dr<N and -1<c-dc<M and ls[r-dr][c-dc] != 1:
            r-=dr
            c-=dc
        else:
            print(cnt)
            exit()