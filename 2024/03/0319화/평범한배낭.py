# https://www.acmicpc.net/problem/12865
# 시간 초과
import sys
input = sys.stdin.readline


N, K = map(int, input().rstrip('\n').split())
ls = []
for i in range(N):
    ls.append(list(map(int, input().rstrip('\n').split())))
# ls.sort(key=lambda x: x[0], reverse=True)

dp = {
    0: 0
}
for w, v in ls:
    temp = list(dp.keys())
    temp_d = {}
    for k in temp:
        if k+w <= K:
            temp_d[k+w] = max(dp.get(k, 0)+v, dp.get(k+w, 0))
    dp.update(temp_d)

# print(dp)
print(max(dp.values()))
