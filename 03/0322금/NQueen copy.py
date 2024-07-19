N = int(input())

cnt = 0


def is_diagonal(i, j, visited):
    for r, c in visited:
        if abs(r - i) == abs(c - j):
            return True
    return False


def dfs(row, visited):
    global cnt, N
    if row == N:  # 모든 행을 다 확인한 경우
        cnt += 1
        return
    for col in range(N):
        if col not in [c for _, c in visited] and not is_diagonal(row, col, visited):
            visited.append((row, col))  # 현재 위치를 방문 목록에 추가
            dfs(row + 1, visited)  # 다음 행으로 진행
            visited.pop()  # 백트래킹: 현재 위치를 다시 제거하여 다른 경우를 탐색


# 각 행에서 시작하여 DFS를 수행
for col in range(N):
    dfs(1, [(0, col)])  # 첫 번째 행을 고정하고 DFS 시작

print(cnt)
