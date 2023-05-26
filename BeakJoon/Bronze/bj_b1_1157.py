# 1157

# word = input().upper()

# counts = {}

# for a in word:
#     if a.isalpha():
#         if a in counts:
#             counts[a] += 1
#         else:
#             counts[a] = 1

# result = [a for a,cnt in counts.items() if cnt == max(counts.values())]

# if len(result) != 1:
#     print('?')
# else:
#     print(result[0])

from collections import deque

def bfs(grid, visited, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start_row, start_col)])  # BFS를 위한 큐
    visited[start_row][start_col] = True  # 시작 위치 방문 체크

    stars_count = 0  # 방문한 별의 개수

    while queue:
        row, col = queue.popleft()

        if grid[row][col] == '*':
            stars_count += 1

        # 상하좌우 이동
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc

            if (new_row < 0 or new_row >= rows or
                new_col < 0 or new_col >= cols or
                grid[new_row][new_col] == '#' or
                visited[new_row][new_col]):
                continue

            visited[new_row][new_col] = True
            queue.append((new_row, new_col))

    return stars_count


h, w = map(int, input().split())  # 격자의 높이와 너비 입력
grid = [input() for _ in range(h)]  # 격자 입력

# 공의 위치와 별의 위치 찾기
ball_row, ball_col = -1, -1
stars_count = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'O':
            ball_row, ball_col = i, j
        elif grid[i][j] == '*':
            stars_count += 1

visited = [[False] * w for _ in range(h)]  # 방문 여부를 저장하는 2차원 리스트

visited_stars = bfs(grid, visited, ball_row, ball_col)

if visited_stars == stars_count:
    print("YES")
else:
    print("NO")



