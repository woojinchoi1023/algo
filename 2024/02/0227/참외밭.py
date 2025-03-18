# 참외밭

# import sys

# sys.stdout = open('/stdout.txt', 'w')

K = int(input())
ls = [list(map(int, input().split()))for _ in range(6)]
board = [[0]*1001 for i in range(1001)]
r, c = 500, 500
d = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0),
}


for direction, dist in ls:
    # if direction != 1:
    # cnt += dist  # 테두리도 포함
    # cnt += dist
    dr, dc = d[direction]
    for i in range(dist):
        if -1 < r+dr*i < 1001 and -1 < c+dc*i < 1001:
            # print('draw')
            board[r+dr*i][c+dc*i] = 1
    r, c = r+dr*dist, c+dc*dist

cnt = 0
for i in range(1001):
    found = False
    for j in range(1001):
        if board[i][j] == 0 and found:
            cnt += 1
        if board[i][j] == 1 and not found:
            found = True
        elif board[i][j] == 1 and found:
            break
for i in range(1001):
    for j in range(1001):
        if board[i][j] == 1:
            cnt += 1

print(cnt)

# for i in board:
#     print(*i, sep='')

# sys.stdout.close()
