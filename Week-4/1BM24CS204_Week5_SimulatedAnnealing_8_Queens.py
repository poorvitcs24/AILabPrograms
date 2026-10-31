
import random
import math

# Calculate the number of attacking queen pairs
def calculate_cost(state):
    cost = 0

    for i in range(8):
        for j in range(i + 1, 8):

            # Check diagonal attacks
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Generate a random neighboring state
def get_neighbor(state):
    neighbor = state.copy()

    col = random.randint(0, 7)
    new_row = random.randint(0, 7)

    while new_row == neighbor[col]:
        new_row = random.randint(0, 7)

    neighbor[col] = new_row

    return neighbor


# Simulated Annealing Algorithm
def simulated_annealing():

    # Generate initial random state
    current = [0, 4, 7, 5, 2, 6, 1, 0]

    # Initial temperature
    T = 100

    # Cooling rate
    cooling_rate = 0.95

    while T > 0.001:

        current_cost = calculate_cost(current)

        print("\nCurrent State:", current)
        print("Current Cost:", current_cost)
        print("Temperature:", round(T, 3))

        # Check goal condition
        if current_cost == 0:
            print("\nGoal State Reached!")
            break

        # Generate neighboring state
        next_state = get_neighbor(current)

        next_cost = calculate_cost(next_state)

        # Calculate change in energy
        delta_E = current_cost - next_cost

        # Accept better state
        if delta_E > 0:
            current = next_state

        # Accept worse state with probability
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        # Decrease temperature
        T = T * cooling_rate

    # Display final result
    print("\nFinal Configuration:", current)
    print("Final Cost:", calculate_cost(current))

    if calculate_cost(current) == 0:
        print("8-Queens Solution Found!")
    else:
        print("Solution Not Found!")


# Execute the algorithm
simulated_annealing()
