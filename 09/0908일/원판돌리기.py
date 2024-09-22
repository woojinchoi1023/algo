# https://www.acmicpc.net/problem/17822

from collections import deque
N, M, T = map(int, input().split())


ls = [deque() for _ in range(N+1)]

totalCnt = N*M
totalSum = 0

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    ls[i].extend(temp)
    totalSum += sum(temp)

for _ in range(T):
    x, d, k = map(int, input().split())
    # x 배수인 원판을 d 방향으로 k칸 회전... d=1이면 -k
    for i in range(x, N+1, x):
        if d:
            ls[i].rotate(-1*k)
        else:
            ls[i].rotate(k)

    same = set()
    for r in range(1, N+1):
        for c in range(M):
            if ls[r][c] == 0:
                continue
            if ls[r][c] == ls[r][(c+1) % M]:
                same.add((r, c))
                same.add((r, (c+1) % M))
            if r+1 < N+1 and ls[r][c] == ls[r+1][c]:
                same.add((r, c))
                same.add((r+1, c))

    if len(same) > 0:
        for r, c in same:
            totalCnt -= 1
            totalSum -= ls[r][c]
            ls[r][c] = 0
    else:
        avg = 0  # zerodivision error
        if totalCnt:
            avg = totalSum/totalCnt
        for r in range(1, N+1):
            for c in range(M):
                if ls[r][c] == 0:
                    continue
                if ls[r][c] > avg:
                    ls[r][c] -= 1
                    totalSum -= 1
                elif ls[r][c] < avg:
                    ls[r][c] += 1
                    totalSum += 1

print(totalSum)


'''
1 1 2 3
2 5 2 4
3 1 3 5

'''
