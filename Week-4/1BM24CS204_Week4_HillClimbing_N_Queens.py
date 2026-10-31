from itertools import combinations

# Calculate the number of attacking queen pairs
def calculate_cost(state):
    cost = 0

    for i in range(4):
        for j in range(i + 1, 4):

            # Check diagonal attack
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Generate neighbouring states by swapping queen positions
def get_neighbors(state):
    neighbors = []

    for i, j in combinations(range(4), 2):
        new_state = state.copy()

        new_state[i], new_state[j] = new_state[j], new_state[i]

        neighbors.append((new_state, (i, j)))

    return neighbors


# Hill Climbing Algorithm
def hill_climbing():

    current = [3, 1, 2, 0]

    while True:

        current_cost = calculate_cost(current)

        print("\nCurrent State:", current)
        print("Current Cost:", current_cost)

        # Check goal condition
        if current_cost == 0:
            print("Goal State Reached!")
            break

        neighbors = get_neighbors(current)

        print("\nNeighbor States:")

        for state, swap in neighbors:
            print("Swap", swap,
                  "State:", state,
                  "Cost:", calculate_cost(state))

        # Select minimum-cost neighbor.
        # combinations() generates pairs in tie-breaking order.
        best_state, best_swap = min(
            neighbors,
            key=lambda item: calculate_cost(item[0])
        )

        best_cost = calculate_cost(best_state)

        # Stop if no improvement is possible
        if best_cost >= current_cost:
            print("\nNo better neighbor found.")
            print("Algorithm Terminated.")
            break

        print("\nSelected Swap:", best_swap)

        current = best_state

    print("\nFinal Configuration:", current)
    print("Final Cost:", calculate_cost(current))


hill_climbing()