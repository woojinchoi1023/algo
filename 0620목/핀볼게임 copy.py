# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&&
# 5650. [모의 SW 역량테스트] 핀볼 게임

# 49개

T = int(input())

# Directions: 0=Up, 1=Down, 2=Left, 3=Right
direction = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1),
}

rev = {
    0: 1,
    1: 0,
    2: 3,
    3: 2,
}

block = {
    1: {0: 1, 1: 3, 2: 0, 3: 2},
    2: {0: 3, 1: 0, 2: 1, 3: 2},
    3: {0: 2, 1: 0, 2: 3, 3: 1},
    4: {0: 1, 1: 2, 2: 3, 3: 0},
    5: {0: 1, 1: 0, 2: 3, 3: 2},
}


def sol(r, c, d):
    cnt = 0
    start = (r, c)
    dr, dc = direction[d]

    # If starting position is immediately out of bounds
    if not (0 <= r + dr < N and 0 <= c + dc < N):
        return 1  # 이것 때문에 50번째 틀렸었음 ㅠㅠ

    while True:
        dr, dc = direction[d]
        nr, nc = r + dr, c + dc

        # If we return to the starting point
        if (nr, nc) == start:
            return cnt

        if 0 <= nr < N and 0 <= nc < N:
            r, c = nr, nc
            if ls[r][c] == -1:  # Black hole
                return cnt
            elif 1 <= ls[r][c] <= 5:  # Block
                d = block[ls[r][c]][d]
                cnt += 1
            elif 6 <= ls[r][c] <= 10:  # Wormhole
                cand = wormhole[ls[r][c]]
                for i, j in cand:
                    if (i, j) != (r, c):
                        r, c = i, j
                        break
            # Empty space, continue in the same direction
        else:  # Wall, reverse direction
            d = rev[d]
            cnt += 1
            # Additional check for blocks adjacent to walls
            if 1 <= ls[r][c] <= 5:
                d = block[ls[r][c]][d]
                cnt += 1
            elif 6 <= ls[r][c] <= 10:  # Wormhole
                cand = wormhole[ls[r][c]]
                for i, j in cand:
                    if (i, j) != (r, c):
                        r, c = i, j
                        break


for t in range(T):
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(list(map(int, input().split())))

    wormhole = {i: [] for i in range(6, 11)}

    for i in range(N):
        for j in range(N):
            if 6 <= ls[i][j] <= 10:
                wormhole[ls[i][j]].append((i, j))

    ans = 0

    for r in range(N):
        for c in range(N):
            if ls[r][c] != 0:
                continue
            for d in range(4):  # Directions: 0=Up, 1=Down, 2=Left, 3=Right
                temp = sol(r, c, d)
                if temp > ans:
                    ans = temp

    print(f'#{t+1} {ans}')
