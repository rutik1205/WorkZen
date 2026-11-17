
from collections import deque

# Goal State
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Function to print puzzle
def print_puzzle(state):
    for row in state:
        for val in row:
            if val == 0:
                print("_", end=" ")
            else:
                print(val, end=" ")
        print()
    print()

# Function to check goal state
def is_goal(state):
    return state == goal_state

# Function to find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_states(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    children = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            # Copy current state
            new_state = [row[:] for row in state]

            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            children.append(new_state)

    return children

def bfs(initial_state):
    queue = deque()
    visited = set()

    queue.append((initial_state, 0))

    while queue:
        current_state, level = queue.popleft()

        # Convert state to tuple for visited set
        state_tuple = tuple(map(tuple, current_state))

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        print("Level:", level)
        print_puzzle(current_state)

        # Goal Check
        if is_goal(current_state):
            print("Goal State Reached!")
            return

        # Generate child states
        for child in generate_states(current_state):
            queue.append((child, level + 1))

    print("Solution not found.")

# Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Initial State:")
print_puzzle(initial_state)

# Run BFS
bfs(initial_state)
