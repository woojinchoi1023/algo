# https://www.acmicpc.net/problem/3430
# import heapq
Z = int(input())
for _ in range(Z):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    zeros = []
    g = {i: [] for i in range(1, N+1)}  # 각 번호의 idx 저장, 100만
    # g = [-1] * (N+1)
    for i in range(M):
        if ls[i] == 0:
            zeros.append([i, 0])  # idx, value
        else:
            g[ls[i]].append(i)
            # if g[ls[i]] != -1:

    zidx = len(zeros)-1

    for i in range(M-1, -1, -1):
        pond = ls[i]
        if pond == 0:
            continue
        g[pond].pop()  # delete current idx

        prev = -1
        if g[pond]:  # 전에꺼가 있으면 불러옴
            prev = g[pond][-1]
        while zidx > -1 and zeros[zidx][0] < prev:
            zidx -= 1

        if zidx < 0:  # no zero left
            print('NO')
            break

        zeros[zidx][1] = pond
        zidx -= 1

    else:
        print('YES')
        for k in zeros:
            print(k[1], end=' ')
        print()


'''

1
2 6
0 0 1 0 2 1

1
2 6
0 0 0 1 0 1


4
2 4
0 0 1 1
2 4
0 1 0 2
2 3
0 1 2
2 4
0 0 0 1




'''
