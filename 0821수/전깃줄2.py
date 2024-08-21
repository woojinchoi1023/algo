# https://www.acmicpc.net/problem/2568

N = int(input())

ls = []

for _ in range(N):
    x, y = map(int, input().split())
    ls.append((x, y))

ls.sort(key=lambda x: x[0])

# print(ls)

cnt = [0]*N
con = {i: set() for i in range(N)}
for i in range(N):
    a, b = ls[i]
    for j in range(i+1, N):
        c, d = ls[j]
        if (a-c)*(b-d) < 0:
            cnt[i] += 1
            cnt[j] += 1
            con[i].add(j)
            con[j].add(i)

ans = []
while sum(cnt) > 0:
    mx = max(cnt)
    mxIdx = cnt.index(mx)
    ans.append(mxIdx+1)
    # print(cnt, mxIdx)
    others = con[mxIdx]
    for i in others:
        con[i].remove(mxIdx)
        cnt[i] -= 1
    cnt[mxIdx] = 0

ans.sort()
for i in ans:
    print(i)
