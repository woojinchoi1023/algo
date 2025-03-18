# https://www.acmicpc.net/problem/1052
N, M = map(int, input().split())

g = {i: 0 for i in range(25)}


b = bin(N)[2:][::-1]
for i in range(len(b)):
    if b[i] == '1':
        g[i] = 1

# print(g)

ans = 0
while sum(g.values()) > M:
    for i in range(24):
        if g[i] > 0:
            if g[i] % 2 == 0:
                g[i+1] += g[i]//2
                g[i] = 0
                break
            else:
                ans += 2**i
                g[i] += 1
                break
    # print(g, ans)
print(ans)
