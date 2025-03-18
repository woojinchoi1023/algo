# https://www.acmicpc.net/problem/25312

import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = []
for _ in range(N):
    w, v = map(int, input().split())
    ls.append((w, v))
ls.sort(key=lambda x: (x[1]/x[0]))
child = mother = 0
cnt = 0
while cnt < M:
    w, v = ls.pop()
    add = min(w, M-cnt)
    cnt += add
    l = math.lcm(mother, w)
    mother = l
    child = child

# # print(sugar)
# temp = str(sugar)
# temp_ls = temp.split('.')
# # print(len(temp_ls[-1]))
# mother = 10**len(temp_ls[-1])
# child = 10**len(temp_ls[-1]) * sugar
# child = int(child)
# while True:
#     for i in [2, 5]:
#         if child % i == 0 and mother % i == 0:
#             child //= i
#             mother //= i
#             break
#     else:
#         break

# print(child, '/', mother, sep='')
