
from collections import deque

# Check whether state is valid
def is_valid(m_left, c_left, m_right, c_right):
    # Missionaries should not be outnumbered
    if (m_left > 0 and c_left > m_left):
        return False
    if (m_right > 0 and c_right > m_right):
        return False

    # Values should not be negative
    if min(m_left, c_left, m_right, c_right) < 0:
        return False

    return True


# DFS function
def dfs(state, goal, visited, path):
    if state == goal:
        path.append(state)
        return True

    visited.add(state)
    path.append(state)

    m_left, c_left, boat = state

    # Possible moves
    moves = [
        (2, 0),
        (0, 2),
        (1, 1),
        (1, 0),
        (0, 1)
    ]

    for m, c in moves:

        # Boat on left side
        if boat == 1:
            new_state = (
                m_left - m,
                c_left - c,
                0
            )
        else:
            # Boat on right side
            new_state = (
                m_left + m,
                c_left + c,
                1
            )

        new_m_left, new_c_left, new_boat = new_state

        m_right = 3 - new_m_left
        c_right = 3 - new_c_left

        if is_valid(new_m_left, new_c_left,
                   m_right, c_right):

            if new_state not in visited:

                if dfs(new_state, goal,
                       visited, path):
                    return True

    path.pop()
    return False


# Initial and Goal states
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

visited = set()
path = []

# Run DFS
if dfs(initial_state, goal_state,
        visited, path):

    print("Solution Found:\n")

    for step in path:
        m, c, b = step

        side = "Left" if b == 1 else "Right"

        print(f"Missionaries Left: {m}, "
              f"Cannibals Left: {c}, "
              f"Boat: {side}")

else:
    print("No solution found.")
