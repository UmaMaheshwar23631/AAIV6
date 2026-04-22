import heapq

def heuristic(state, goal):
    return goal - state

def astar(start, goal):
    heap = [(0 + heuristic(start, goal), 0, start, [start])]
    visited = set()

    while heap:
        f, g, state, path = heapq.heappop(heap)

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in [state + 1, state + 2]:
                if next_state <= goal:
                    new_g = g + 1
                    new_f = new_g + heuristic(next_state, goal)
                    heapq.heappush(heap, (new_f, new_g, next_state, path + [next_state]))

print("A* Path:", astar(0, 10))