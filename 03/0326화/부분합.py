# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
ls = list(map(int, input().split()))
i = j = s = 0  # i부터 j까지 합
minv = N+1
s += ls[j]
while i < N:
    if s < S:  # 작으면
        if j < N-1:  # 남아있고
            j += 1  # 오른쪽 하나 이동
            s += ls[j]
        else:  # 남아있는게 없으면 끝
            break
    else:  # 크면
        if minv > j-i+1:  # 길이
            minv = j-i+1
        s -= ls[i]  # 왼쪽 하나 이동
        i += 1

if minv == N+1:  # 한번도 업데이트 되지 않았으면 0
    minv = 0
print(minv)
