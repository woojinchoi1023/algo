# https://www.acmicpc.net/problem/9328
T = int(input())

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for t in range(T):
    h, w = map(int, input().split())
    ls = [list(input())for _ in range(h)]
    keys = {i.upper() for i in input()}

    # 가장자리 바깥에서 시작
    st = [(r, c)for r in range(-1, h+1)
          for c in range(-1, w+1) if r == -1 or r == h or c == -1 or c == w]

    visited = [[0]*w for _ in range(h)]

    locked = []
    cnt = 0
    while True:
        while st:
            r, c = st.pop()
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                if -1 < nr < h and -1 < nc < w and visited[nr][nc] == 0 and ls[nr][nc] != '*':
                    if ls[nr][nc] == '$':
                        cnt += 1
                    elif 'a' <= ls[nr][nc] <= 'z':
                        keys.add(ls[nr][nc].upper())
                    elif 'A' <= ls[nr][nc] <= 'Z':
                        if ls[nr][nc] in keys:
                            pass
                        else:
                            locked.append((nr, nc))
                            visited[nr][nc] = 1
                            continue
                    st.append((nr, nc))
                    visited[nr][nc] = 1

        if not locked:
            print(cnt)
            break
        else:
            temp = []
            for r, c in locked:
                if ls[r][c] in keys:
                    st.append((r, c))
                else:
                    temp.append((r, c))
            locked = temp
            # print(st, keys)
            if not st:
                print(cnt)
                break
