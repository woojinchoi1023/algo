# https://www.acmicpc.net/problem/9095

T = int(input())
d = {
    1: 1,
    2: 2,
    3: 4,
}
for t in range(T):
    n = int(input())
    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]
    print(d[n])
