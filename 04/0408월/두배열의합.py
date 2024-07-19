# https://www.acmicpc.net/problem/2143

import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def twopointers(s):
    cnt = 0
    p = q = 0
    d = B[0]
    while q < M and p < M:
        d = sum(B[p:q+1])
        # print(p, q, d)
        if s+d == T:
            cnt += 1
            p += 1
            q += 1
            continue
        if s+d < T:
            q += 1
        else:
            p += 1
    return cnt


i = j = 0
cnt = 0
while j < N and i < N:
    # print(i, j, cnt)
    s = sum(A[i:j+1])
    if s >= T:
        i += 1
        continue
    cnt += twopointers(s)

    if i == j:
        j += 1
    else:
        i += 1
print(cnt)
