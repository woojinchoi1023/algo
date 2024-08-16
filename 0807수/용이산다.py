# https://www.acmicpc.net/problem/3430
from heapq import heappop, heappush


def sol():
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    hq = []
    ans = []
    d = dict()
    for i in range(M):
        num = ls[i]
        if num == 0:
            heappush(hq, (M-i, i))
        else:
            after = d.get(num, -1)
            if not hq:
                print('NO')
                return
            _, z = heappop(hq)
            if after > z:
                print('NO')
                return
            heappush(ans, (z, num))
            d[num] = i

    print('YES')
    while hq:
        _, z = heappop(hq)
        heappush(ans, (z, 0))
    while ans:
        a, b = heappop(ans)
        print(b, end=' ')
    print()


T = int(input())
for t in range(T):
    sol()
'''
1
2 6
0 0 1 0 2 1

1
2 6
0 0 0 1 0 1

1 1 x 2 x x
1 2 x 1 x
    x 1 x x
'''
