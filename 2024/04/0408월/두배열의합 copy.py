# https://www.acmicpc.net/problem/2143

import sys
input = sys.stdin.readline

T = float(input())
N = int(input())
A = list(map(float, input().split()))
M = int(input())
B = list(map(float, input().split()))

'''
-5
3
-5 0 0
3
0 1 1
'''

d = {}
for i in range(M):
    s = 0
    for j in range(i, M):
        s += B[j]
        d.setdefault(s, 0)
        d[s] += 1
# print(d)

cnt = 0
for i in range(N):
    s = 0
    for j in range(i, N):
        s += A[j]
        cnt += d.get(T-s, 0)
print(cnt)
