# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&&
# 5650. [모의 SW 역량테스트] 핀볼 게임

# 48개


T = int(input())

# 상하좌우 0123
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

block = {  # block[blockCode][direction] = new direction
    1: {
        0: 1,  # 위 방향 -> 아래 방향
        1: 3,  # 아래 -> 오른쪽
        2: 0,  # 좌 -> 위
        3: 2,  # 우 -> 좌
    },
    2: {
        0: 3,
        1: 0,
        2: 1,
        3: 2,
    },
    3: {
        0: 2,
        1: 0,
        2: 3,
        3: 1,
    },
    4: {
        0: 1,
        1: 2,
        2: 3,
        3: 0,
    },
    5: {
        0: 1,
        1: 0,
        2: 3,
        3: 2,
    },
}


def sol(r, c, d):
    cnt = 0
    start = (r, c)

    # 벽 보고 스타트 하면 안됨?
    dr, dc = direction[d]
    if not (-1 < r+dr < N and -1 < c+dc < N):
        return 0

    while True:
        # print(r, c, d, cnt)
        # if cnt > 10:
        #     return cnt
        dr, dc = direction[d]
        if (r+dr, c+dc) == start:  # 돌아오면 끝
            return cnt
        if -1 < r+dr < N and -1 < c+dc < N:
            r += dr
            c += dc
            if ls[r][c] == -1:  # 블랙홀
                return cnt
            elif 1 <= ls[r][c] <= 5:  # 블록
                d = block[ls[r][c]][d]
                cnt += 1
            elif 6 <= ls[r][c] <= 10:  # 웜홀
                cand = wormhole[ls[r][c]]
                for i, j in cand:
                    if i != r and j != c:
                        r, c = i, j
                        break
            else:  # 빈 공간
                pass

        else:  # 벽이니까 뒤집기
            d = rev[d]
            cnt += 1
            if 1 <= ls[r][c] <= 5:  # 블록... 반례: 벽에 붙어있는 블록
                d = block[ls[r][c]][d]
                cnt += 1
            elif 6 <= ls[r][c] <= 10:  # 웜홀
                cand = wormhole[ls[r][c]]
                for i, j in cand:
                    if i != r and j != c:
                        r, c = i, j
                        break


for t in range(T):
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(list(map(int, input().split())))

    wormhole = {
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],

    }
    for i in range(N):
        for j in range(N):
            if 6 <= ls[i][j] <= 10:
                wormhole[ls[i][j]].append((i, j))

    # print(wormhole)
    ans = 0

    # ans = sol(4, 0, 2)

    for r in range(N):
        for c in range(N):
            if ls[r][c] != 0:
                continue
            for d in range(4):  # direction
                temp = sol(r, c, d)
                # print(r, c, d, temp)
                if temp > ans:
                    ans = temp

    print(f'#{t+1}', ans)
