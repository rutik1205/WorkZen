
goal = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = []
            for row in state:
                new_state.append(row[:])
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)
    return result

def astar(start):
    open_list = [(start, 0)]
    visited = []

    while open_list:
        best = 0
        best_f = open_list[0][1] + heuristic(open_list[0][0])
        for i in range(len(open_list)):
            state, g = open_list[i]
            f = g + heuristic(state)
            if f < best_f:
                best = i
                best_f = f
        state, g = open_list.pop(best)
        if state in visited:
            continue
        visited.append(state)
        print("Current State:")
        for row in state:
            print(row)
        print()
        if state == goal:
            print("Goal Reached!")
            return
        for child in neighbors(state):
            if child not in visited:
                open_list.append((child, g + 1))

start = [[1,2,3],
          [4,0,6],
          [7,5,8]]

astar(start)
