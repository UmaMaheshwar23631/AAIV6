from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in [state + 1, state + 2]:
                if next_state <= goal:
                    queue.append((next_state, path + [next_state]))

print("BFS Path:", bfs(0, 10))