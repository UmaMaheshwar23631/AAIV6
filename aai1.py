def create_state_space(start, goal):
    state_space = {}

    for state in range(start, goal + 1):
        next_states = []

        if state + 1 <= goal:
            next_states.append(state + 1)

        if state + 2 <= goal:
            next_states.append(state + 2)

        state_space[state] = next_states

    return state_space


# Create state space from 0 to 10
graph = create_state_space(0, 10)

# Print state space
for state, transitions in graph.items():
    print(f"{state} -> {transitions}")