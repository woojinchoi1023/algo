# https://www.acmicpc.net/problem/3430
from collections import deque
import bisect
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    d = set()
    zeros = 0
    zidx = deque()
    for i in range(M-1, -1, -1):
        temp = ls[i]
        if temp:
            if temp in d:
                if zeros > 0:
                    zeros -= 1
                    d.remove(temp)
                else:
                    print('NO')
                    break
            else:
                d.add(temp)
        else:
            zeros += 1
            zidx.appendleft(i)
    else:
        if len(zidx) < len(d):
            print('NO')
            continue
        z = [0] * len(zidx)
        # print('zidx=', zidx)
        for i in range(M):
            temp = ls[i]
            if temp:
                res = bisect.bisect_left(zidx, i)
                # print('res=', res, i)
                if res > 0:
                    res -= 1
                while res >= len(z) or z[res] != 0:
                    # print(temp, res)
                    res -= 1
                z[res] = temp
        print('YES')
        print(*z)


'''
1
2 6
0 1 0 2 0 1
  
1
3 6
0 0 0 1 2 3

1
3 9
0 0 0 1 2 3 0 0 0
'''
