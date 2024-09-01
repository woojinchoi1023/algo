# 1620 나는야 포켓몬 마스터
import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
d = {}
for i in range(N):
    s = sys.stdin.readline().rstrip('\n')
    d[i+1] = s
    d[s] = i+1
for j in range(M):
    q = sys.stdin.readline().rstrip('\n')
    if q.isdigit():
        print(d[int(q)])
    else:
        print(d[q])
