# https://www.acmicpc.net/problem/13549
from collections import deque


def bfs(start, target):
    visited = [-1] * 100001
    visited[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == target:
            return visited[current]

        next_positions = [current*2, current-1, current+1]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                if next_pos == current*2:
                    visited[next_pos] = visited[current]
                    # Put the doubled position to the front of the queue for immediate exploration
                    queue.appendleft(next_pos)
                else:
                    visited[next_pos] = visited[current] + 1
                    queue.append(next_pos)


N, K = map(int, input().split())
print(bfs(N, K))
