import heapq

initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Calculate Manhattan distance (excluding blank)
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = goal.index(tile)

            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_pos, 3)

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


# Generate valid next states
def get_neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[blank], new_state[pos] = (
                new_state[pos], new_state[blank]
            )
            yield tuple(new_state)


# A* algorithm
def astar():
    open_list = [(heuristic(initial), 0, initial)]
    parent = {initial: None}
    g_score = {initial: 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if g != g_score[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Solution using Manhattan Distance:")
            print("Total moves:", len(path) - 1)

            for step, state in enumerate(path):
                h = heuristic(state)
                print(f"\nStep {step}: g={step}, h={h}, f={step+h}")
                for i in range(0, 9, 3):
                    print(state[i:i+3])
            return

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if new_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(open_list, (new_f, new_g, neighbor))

    print("No solution found.")


astar()