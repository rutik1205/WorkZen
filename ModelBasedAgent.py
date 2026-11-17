from collections import deque

grid = [
    ['A', '.', 'X', 'X'],
    ['X', '.', '.', '.'],
    ['.', '.', 'X', 'G']
]

start, goal = (0, 0), (2, 1)
directions = [
        (-1, 0, "UP"), (1, 0, "DOWN"),
        (0, -1, "LEFT"), (0, 1, "RIGHT")
    ]


def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start, [])])
    visited = {start}

   

    while q:
        (x, y), path = q.popleft()

        if (x, y) == goal:
            return path

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 0 <= ny < cols
                    and grid[nx][ny] != 'X'
                    and (nx, ny) not in visited):

                visited.add((nx, ny))
                q.append(((nx, ny), path + [move]))

    return None

print("Initial Grid\n")
for row in grid:
    print(row)
    print()
print("Path to Goal:")
print(bfs(grid, start, goal))