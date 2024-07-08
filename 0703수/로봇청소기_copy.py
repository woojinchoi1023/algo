# https://www.acmicpc.net/problem/4991

while True:
    M, N = map(int, input().split())
    if N == M == 0:
        exit()
    ls = [list(input()) for _ in range(N)]
    # print(*ls, sep='\n')
    trash = []
    start = (-1, -1)
    for r in range(N):
        for c in range(M):
            if ls[r][c] == '*':
                trash.append((r, c))
            elif ls[r][c] == 'o':
                start = (r, c)

    print(trash)
