# 1074 Z
d = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 2,
    (1, 1): 3,
}


def z(N):
    global r, c, cnt
    if N == 1:
        cnt += d[(r, c)]
        print(cnt)
        return
    if r >= 2**(N-1) and c >= 2**(N-1):  # 4th
        r -= 2**(N-1)
        c -= 2**(N-1)
        cnt += ((2**(N-1))**2)*3
    elif r >= 2**(N-1):  # 3rd
        r -= 2**(N-1)
        cnt += ((2**(N-1))**2)*2
    elif c >= 2**(N-1):  # 2nd
        c -= 2**(N-1)
        cnt += ((2**(N-1))**2)*1
    z(N-1)


N, r, c = map(int, input().split())
cnt = 0
z(N)
