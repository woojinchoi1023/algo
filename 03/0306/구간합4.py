# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip('\n').split())
ls = list(map(int, input().rstrip('\n').split()))
# d = {}
# for i in range(N):
#     d[i] = ls[i]
# for j in range(M):
#     a, b = map(int, input().rstrip('\n').split())
#     print(sum(d[i] for i in range(a-1, b)))
for i in range(1, N):
    ls[i] += ls[i-1]  # cumul
# print(ls)
for j in range(M):
    a, b = map(int, input().rstrip('\n').split())
    if a == 1:
        print(ls[b-1])
    else:
        print(ls[b-1]-ls[a-2])
