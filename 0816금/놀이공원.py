# https://www.acmicpc.net/problem/1561
'''
3 5
7 8 9 7 8
3

7 2
3 2
2

--->6
2, 3, 2


22 5
1 2 3 4 5
4

-->8
5 + 8 + 4+ 2+2+1

'''
N, M = map(int, input().split())

ls = list(map(int, input().split()))

g = {i: [] for i in range(1, 31)}
for i in range(M):
    dur = ls[i]
    g[dur].append(i+1)


def sol(t):
    cnt = M
    for i in range(1, 31):
        cnt += t//i*len(g[i])
    return cnt


bot, top = 0, 2*10e9*30
ans = float('inf')
while bot <= top:
    mid = (bot+top)//2
    res = sol(mid)
    # print(mid, res)
    if res >= N:
        top = mid-1
        ans = min(ans, mid)
    else:
        bot = mid+1

# print(ans)
if ans == 0:
    print(N)
    exit()

# ans-1 까지
cnt = M
for i in range(1, 31):
    cnt += (ans-1)//i*len(g[i])
cand = []
for i in range(1, 31):
    if ans % i == 0:
        cand.extend(g[i])
cand.sort()
# print(N, cnt, cand)
print(cand[int(N-cnt-1)])
