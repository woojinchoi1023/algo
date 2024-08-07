# https://www.acmicpc.net/problem/3430
from collections import deque
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    zeros = 0
    d = []
    ans = deque()
    for i in range(M-1, -1, -1):
        temp = ls[i]
        if temp:
            if temp in d:
                if zeros > 0:
                    zeros -= 1
                    d.remove(temp)
                    ans.appendleft(temp)
                else:
                    print('NO')
                    break
            else:
                d.append(temp)
        else:
            zeros += 1
    else:
        if len(d) > zeros:
            print('NO')
        else:
            print('YES')
            for j in d:
                ans.appendleft(j)
            for k in range(zeros-len(d)):
                ans.appendleft(0)
            print(*ans)
