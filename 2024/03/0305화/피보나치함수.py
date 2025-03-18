# 1003 피보나치

T = int(input())
dp1 = {
    0: 0,
    1: 1,
}
dp0 = {
    0: 1,
    1: 0,
}
for t in range(T):
    N = int(input())
    for i in range(1, N+1):
        if not dp1.get(i):
            dp1[i] = dp1[i-2]+dp1[i-1]
            dp0[i] = dp0[i-2]+dp0[i-1]
    print(dp0[N], dp1[N])
