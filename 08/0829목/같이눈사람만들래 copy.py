# https://www.acmicpc.net/problem/20366
# pypy3 로만 통과됨

import sys

input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

ls.sort()

minV = float('inf')

for a in range(N-3):
    for d in range(a+3, N):
        sum1 = ls[a] + ls[d]  # python3
        b, c = a+1, d-1
        while b < c:
            sum2 = ls[b] + ls[c]
            minV = min(minV, abs(sum1-sum2))
            if sum1 == sum2:  # python3
                print(0)
                exit()
            if sum1-sum2 > 0:
                b += 1
            else:
                c -= 1
print(minV)
