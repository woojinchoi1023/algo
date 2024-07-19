# https://www.acmicpc.net/problem/20055

from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
u, d = 0, N-1
for a in A:
    dq.append([0, a])
zero = 0
stage = 1
while True:
    dq.rotate(1)
    dq[N-1][0] = 0  # 도착하면 내림
    for i in range(N-2, -1, -1):
        if dq[i][0]:  # 로봇이 있는 경우
            if dq[i+1][0] == 0 and dq[i+1][1]:  # 이동
                dq[i][0] = 0
                dq[i+1][1] -= 1
                if i+1 != N-1:  # 내리는 위치면 걍 사라짐
                    dq[i+1][0] = 1
                if dq[i+1][1] == 0:
                    zero += 1
                    if zero == K:
                        print(stage)
                        exit()
    if dq[0][0] == 0 and dq[0][1]:
        dq[0][0] = 1
        dq[0][1] -= 1
        if dq[0][1] == 0:
            zero += 1
            if zero == K:
                print(stage)
                exit()
    stage += 1
