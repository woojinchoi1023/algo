# https://www.acmicpc.net/problem/9465

T = int(input())
for _ in range(T):
    n = int(input())

    d1 = {}
    d2 = {}
    d3 = {}  # not select

    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))

    d1[0] = ls1[0]
    d2[0] = ls2[0]
    d3[0] = 0
    for i in range(1, n):
        d1[i] = max(d2[i-1], d3[i-1]) + ls1[i]
        d2[i] = max(d1[i-1], d3[i-1]) + ls2[i]
        d3[i] = max(d1[i-1], d2[i-1])
    # print(d1, d2, d3)
    print(max(d1[n-1], d2[n-1], d3[n-1],))
