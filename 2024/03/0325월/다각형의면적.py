# https://www.acmicpc.net/problem/2166

N = int(input())
x = [0]*(N+1)
y = [0]*(N+1)
for i in range(N):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b
x[N], y[N] = x[0], y[0]
# print(x, y)
s = 0
for i in range(N):
    s += x[i]*y[i+1]
    s -= x[i+1]*y[i]
s = abs(s)
print(s/2)


# 2 2
# 4 2
# 4 4
# 0 2 4 4 0
# 0 2 2 4 0
# 4+16-8-8 / 2 = 2

# 0 -2 -1  1 2 1 -1 0
# 0  0 -2 -2 0 2  2 0
# 4 + 2 +4 +2 +2 +4 +2 => 10아님?
