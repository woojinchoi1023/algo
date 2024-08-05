from collections import deque

# Read input
N = int(input())

grid = [list(input()) for _ in range(N)]

heights = [list(map(int, input().split())) for _ in range(N)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

start_row, start_col = 0, 0  # Starting coordinates
house_count = 0

unique_heights = set()
for row in range(N):
    for col in range(N):
        unique_heights.add(heights[row][col])
        if grid[row][col] == 'K':
            house_count += 1
        elif grid[row][col] == 'P':
            start_row, start_col = row, col

unique_heights = sorted(list(unique_heights))


def bfs(start_row, start_col, max_height, min_height):
    queue = deque()
    queue.append((start_row, start_col))
    visited = [[False] * N for _ in range(N)]
    visited[start_row][start_col] = True
    visited_houses = 0

    while queue:
        row, col = queue.popleft()
        if grid[row][col] == 'K':
            visited_houses += 1
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
                if min_height <= heights[new_row][new_col] <= max_height:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

    return visited_houses == house_count


min_difference = float('inf')
num_unique_heights = len(unique_heights)

for i in range(num_unique_heights):
    min_height = unique_heights[i]
    if heights[start_row][start_col] < min_height:
        continue
    left = i
    right = num_unique_heights - 1
    while left <= right:
        mid = (left + right) // 2
        max_height = unique_heights[mid]

        if bfs(start_row, start_col, max_height, min_height):
            min_difference = min(min_difference, max_height - min_height)
            right = mid - 1
        else:
            left = mid + 1

print(min_difference)
