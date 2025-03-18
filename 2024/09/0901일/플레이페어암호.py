# https://softeer.ai/practice/6255

message = input()
key = input()

alphabets = [chr(i) for i in range(65, 91) if i != 74]
temp = list(key) + alphabets
board = {}
boardIdx = [[0]*5 for _ in range(5)]
idx = 0
for r in range(5):
    for c in range(5):
        while board.get(temp[idx], 0) != 0:
            idx += 1
        board[temp[idx]] = (r, c)
        boardIdx[r][c] = temp[idx]

# print(board)
# print(boardIdx)

# make pairs
idx = 0
pairs = []
pair = ''
while idx < len(message):
    if pair:
        if pair != message[idx]:  # H + E
            pairs.append(pair+message[idx])
            pair = ''
        else:
            if pair == 'X':  # X + X
                pairs.append('XQ')
                pair = message[idx]
            else:  # L + L
                pairs.append(pair+'X')
                pair = message[idx]
    else:
        pair = message[idx]
    idx += 1
if pair:  # last one
    pairs.append(pair+'X')

# print(pairs)

# encode
ans = ''
for i in pairs:
    a, b = i[0], i[1]
    ar, ac = board[a]
    br, bc = board[b]
    if ar == br:
        ans += boardIdx[ar][(ac+1) % 5]
        ans += boardIdx[br][(bc+1) % 5]
    elif ac == bc:
        ans += boardIdx[(ar+1) % 5][ac]
        ans += boardIdx[(br+1) % 5][bc]
    else:
        ans += boardIdx[ar][bc]
        ans += boardIdx[br][ac]
print(ans)
