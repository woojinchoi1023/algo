# https://www.acmicpc.net/problem/20056

N, M, K = map(int, input().split())

board = {
    (i, j): [] for i in range(N) for j in range(N)
}
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
         (1, -1), (0, -1), (-1, -1)]  # 인덱스별 방향
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    board[(r-1, c-1)].append((m, s, d))

# move
for _ in range(K):
    newboard = {
        (i, j): [] for i in range(N) for j in range(N)
    }
    for r in range(N):
        for c in range(N):
            if board.get((r, c), []):
                for i in board[(r, c)]:
                    m, s, d = i
                    dr, dc = delta[d]
                    nr, nc = r+s*dr, c+s*dc
                    newboard[(nr % N, nc % N)].append((m, s, d))
    board = newboard
    newboard = {
        (i, j): [] for i in range(N) for j in range(N)
    }
    for r in range(N):
        for c in range(N):
            if len(board[(r, c)]) == 0:
                continue
            elif len(board[(r, c)]) == 1:
                newboard[(r, c)].extend(board[(r, c)])
            else:
                sum_m = 0
                sum_s = 0
                cnt = len(board[(r, c)])
                is_same = True
                is_even = True  # direction
                is_odd = True  # direction
                for i in board[(r, c)]:
                    m, s, d = i
                    if d % 2:
                        is_even = False
                    else:
                        is_odd = False
                    sum_m += m
                    sum_s += s
                nm, ns = sum_m/5, sum_s/cnt
                nm = int(nm)
                ns = int(ns)
                if nm == 0:
                    continue
                if is_odd or is_even:
                    new_delta = [0, 2, 4, 6]
                else:
                    new_delta = [1, 3, 5, 7]
                for d in new_delta:
                    newboard[(r, c)].append((nm, ns, d))
    board = newboard

ans = 0
for r in range(N):
    for c in range(N):
        if board[(r, c)]:
            for m, s, d in board[(r, c)]:
                ans += m
print(ans)

'''
{(0, 0): [], (0, 1): [(2, 1, 6)], (0, 2): [], (0, 3): [(2, 1, 2)], (1, 0): [], (1, 1): [], (1, 2): [(2, 1, 4)], (1, 3): [], (2, 0): [], (2, 1): [], (2, 2): [], (2, 3): [], (3, 0): [], (3, 1): [], (3, 2): [(2, 1, 0)], (3, 3): []}

'''
