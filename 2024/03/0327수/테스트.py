import sys
import time


def writeCheck(r, c, k, v):
    check_row[r][k] = v
    check_col[c][k] = v
    check_square[(r//3)*3+(c//3)][k] = v


def check(r, c, k):
    return check_row[r][k] or check_col[c][k] or check_square[(r//3)*3+(c//3)][k]


def dfs(x, board):
    global start
    if x == len(Position) - 1:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        print(f"{time.time() - start:.10f} sec")

        exit(0)

    r, c = Position[x + 1][0], Position[x + 1][1]
    for num in range(1, 10):
        if check(r, c, num):
            continue
        board[r][c] = num
        writeCheck(r, c, num, True)
        dfs(x + 1, board)
        board[r][c] = 0
        writeCheck(r, c, num, False)


board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
start = time.time()
check_row = [[False]*10 for _ in range(9)]
check_col = [[False]*10 for _ in range(9)]
check_square = [[False]*10 for _ in range(9)]

Position = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            Position.append([i, j])
        else:
            writeCheck(i, j, board[i][j], True)

dfs(-1, board)
