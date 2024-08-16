# https://www.acmicpc.net/problem/1561
import heapq
N, M = map(int, input().split())

ls = list(map(int, input().split()))

g = {i: [] for i in range(1, 31)}
for i in range(M):
    dur = ls[i]
    g[dur].append(i+1)


def sol(time):
    cnt = 0
    # time-1 까지
    for i in range(1, 31):
        cycle = (time-1)//i
        cnt += cycle * len(g[i])
    # time 일때
    cand = []
    for i in range(1, 31):
        if time//i == 0:
            cand.extend(g[i])
    if cnt < N <= cnt+len(cand):
        cand.sort()
    elif cnt >= N:
        return False
    elif cnt+len(cand) < N:
        return False

    return -1


bot, top = 0, 2*10e9*30
while bot < top:
    mid = (bot+top)//2
    sol(mid)

'''
7,8,9

3 2
0:0 1 
2:1 
3:0
4:1
6:1
 
'''
