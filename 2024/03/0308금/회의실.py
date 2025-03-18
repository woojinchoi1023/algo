# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline


N = int(input().rstrip('\n'))
ls = []
for i in range(N):
    ls.append(list(map(int, input().rstrip('\n').split())))
ls.sort(key=lambda x: (x[1], x[0]))
cnt = 0
prev = 0
for i in ls:
    s, e = i
    if s >= prev:
        cnt += 1
        prev = e
        # print('ans', s, e)
print(cnt)
