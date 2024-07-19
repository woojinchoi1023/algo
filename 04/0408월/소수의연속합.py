# https://www.acmicpc.net/problem/1644

import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
    exit()
prime = []
visited = [0]*(N+1)
for i in range(2, N+1):
    if visited[i]:
        continue
    prime.append(i)
    for j in range(i*2, N+1, i):
        visited[j] = 1
# print(visited[:100])
# print(prime)

cnt = 0
i = 0
j = 0
s = prime[j]  # sum
while i <= j:
    # if i == j:
    #     if j+1 == len(prime):
    #         s -= prime[i]
    #         i += 1
    #     else:
    #         j += 1
    #         s += prime[j]
    #     continue
    # print(i, j, s)
    if s == N:
        # print('same', i, j)
        cnt += 1
        if j+1 == len(prime):
            s -= prime[i]
            i += 1
        else:
            j += 1
            s += prime[j]
    elif s > N:
        s -= prime[i]
        i += 1
    else:
        j = min(j+1, len(prime)-1)
        s += prime[j]
print(cnt)
