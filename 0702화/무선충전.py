# 5644. [모의 SW 역량테스트] 무선 충전
T = int(input())
for t in range(T):
    M, A = map(int, input().split())
    board = {
        (i, j): [] for i in range(1, 11) for j in range(1, 11)
    }
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] + a
    b = [0] + b
    for i in range(A):
        x, y, c, p = map(int, input().split())
        for bx, by in board.keys():
            if abs(bx-x)+abs(by-y) <= c:
                board[(bx, by)].append((i, p))  # becon idx, power
    p1, p2 = (1, 1), (10, 10)  # init pos
    # 0: none 1: up 2: right 3: down 4: left
    d = {
        0: (0, 0),
        1: (0, -1),
        2: (1, 0),
        3: (0, 1),
        4: (-1, 0),
    }
    ans = 0
    for i in range(1+M):
        # p1 이동
        direction = a[i]
        dx, dy = d[direction]
        ox, oy = p1
        p1 = (ox+dx, oy+dy)
        # p2 이동
        direction = b[i]
        dx, dy = d[direction]
        ox, oy = p2
        p2 = (ox+dx, oy+dy)
        # 충전 최대값 계산
        mx = 0
        for p1b, p1p in [(-1, 0)]+board[p1]:  # 모든 경우의 수 검사
            for p2b, p2p in [(-1, 0)]+board[p2]:
                if p1b != p2b:
                    temp = p1p+p2p
                else:
                    temp = p1p
                mx = max(mx, temp)
        ans += mx
    print(f'#{t+1}', ans)
