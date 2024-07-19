# 1764 듣보잡
import sys

N, M = map(int, input().split())
a = set()  # 듣도 못한
b = set()  # 보도 못한
for i in range(N):
    a.add(input())
for j in range(M):
    b.add(input())
c = a & b
c = sorted(list(c))
print(len(c), *c, sep='\n')
