# https://www.acmicpc.net/problem/2457
import sys
input = sys.stdin.readline

N = int(input())

ls = []
for i in range(N):
    a, b, c, d = map(int, input().split())
    ls.append([a*100+b, c*100+d])


ls.sort(key=lambda x: (x[0], x[1]))

cnt = 0
end = 301
i, j = 0, 0

if ls[i][0] > 301:  # init
    print(0)
    exit()

while i < N:
    if end > 1130:  # 등호 넣으면 틀림
        break
    tempEnd = ls[i][1]
    j = i+1
    while j < N:
        if ls[j][0] > end:       # stop
            break
        if tempEnd <= ls[j][1]:  # better
            tempEnd = ls[j][1]   # update
            i = j
        j += 1

    if tempEnd > end:
        end = tempEnd
        cnt += 1
    else:
        break

if end > 1130:  # 등호 넣으면 틀림
    print(cnt)
else:
    print(0)

'''

반례 
[[108, 310], [128, 1130], [307, 1210], [319, 520], [706, 904], [904, 1214]]
0 301 0
1
2
1 1130 1
1 1130 1
1

'''
