goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def display(state):
    print()
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    if row > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]

        neighbors.append(("UP", tuple(new_state)))

    if row < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]

        neighbors.append(("DOWN", tuple(new_state)))

    if col > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]

        neighbors.append(("LEFT", tuple(new_state)))

    if col < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]

        neighbors.append(("RIGHT", tuple(new_state)))

    return neighbors

def depth_limited_search(state, depth, path, visited):

    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for move, new_state in get_neighbors(state):

        if new_state not in visited:

            result = depth_limited_search(
                new_state,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None

def ids(initial, max_depth):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            initial,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

    return None

initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)


print("Initial State:")
display(initial)

solution = ids(initial, 20) #instead of 20 iterations, here since soln foulnd level 2 anything above it will give result

if solution is not None:

    print("\nSolution found using IDS!")
    print("Number of moves:", len(solution))
    print("Moves:", solution)

else:

    print("\nNo solution found.")