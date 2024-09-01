# https://www.acmicpc.net/problem/2630

N = int(input())
ls = [list(map(int, input().split()))for i in range(N)]
w = 0
b = 0


def cut(k, r, c):
    global w, b
    if k == 1:
        if ls[r][c] == 0:
            w += 1
        else:
            b += 1
        return
    s = 0
    for row in range(k):
        for col in range(k):
            s += ls[r+row][c+col]
    if s == 0:  # 끝
        w += 1
        return
    elif s == k**2:  # 끝
        b += 1
        return
    else:  # 잘라야함
        cut(k//2, r, c)
        cut(k//2, r, c+k//2)
        cut(k//2, r+k//2, c)
        cut(k//2, r+k//2, c+k//2)


cut(N, 0, 0)
print(w)
print(b)
