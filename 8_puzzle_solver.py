from queue import PriorityQueue

GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                goal_row = (value - 1) // 3
                goal_col = (value - 1) % 3

                distance += abs(i - goal_row) + abs(j - goal_col)

    return distance


# Print Puzzle
def print_state(state):
    for row in state:
        print(*row)
    print()


# Generate Neighbor States
def get_neighbors(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [list(r) for r in state]

            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]

            neighbors.append(tuple(tuple(r) for r in temp))

    return neighbors


# A* Search
def a_star(start):

    pq = PriorityQueue()
    pq.put((manhattan(start), 0, start, [start]))

    visited = set()

    while not pq.empty():

        f, g, state, path = pq.get()

        if state == GOAL:

            print("\n========== A* SEARCH ==========\n")

            for step, board in enumerate(path):
                print("STEP", step)
                print_state(board)

            print("GOAL STATE REACHED")
            print("TOTAL MOVES =", len(path) - 1)
            return

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                h = manhattan(neighbor)

                pq.put((g + h + 1,
                        g + 1,
                        neighbor,
                        path + [neighbor]))


# Greedy Best First Search
def greedy_search(start):

    pq = PriorityQueue()
    pq.put((manhattan(start), start, [start]))

    visited = set()

    while not pq.empty():

        h, state, path = pq.get()

        if state == GOAL:

            print("\n===== GREEDY BEST FIRST SEARCH =====\n")

            for step, board in enumerate(path):
                print("STEP", step)
                print_state(board)

            print("GOAL STATE REACHED")
            print("TOTAL MOVES =", len(path) - 1)
            return

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                pq.put((manhattan(neighbor),
                        neighbor,
                        path + [neighbor]))


# Initial State
START = ((1, 3, 6),
         (5, 0, 2),
         (4, 7, 8))

print("INITIAL STATE\n")
print_state(START)

print("Manhattan Distance =", manhattan(START))

a_star(START)

greedy_search(START)
