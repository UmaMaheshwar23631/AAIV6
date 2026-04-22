def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in [state + 1, state + 2]:
                if next_state <= goal:
                    stack.append((next_state, path + [next_state]))

print("DFS Path:", dfs(0, 10))