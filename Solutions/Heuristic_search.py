import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    """Heuristic: number of tiles out of place (excluding the blank)."""
    mismatch = 0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0 and goal_state[i][j] != state[i][j]:
                mismatch += 1
    return mismatch

def is_goal(state):
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j
                break

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in moves:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def display_state(state, label="", h_cost=None):
    print(f"{label}")
    if h_cost is not None:
        print(f"  [H: {h_cost}]")
    for row in state:
        print("  " + " ".join(str(tile) if tile != 0 else "*" for tile in row))
    print()

def display_frontier(frontier):
    print("Current Frontier (Queue):")
    sorted_frontier = sorted(frontier, key=lambda x: x[0])  # Sort by H
    for idx, (h, state, path) in enumerate(sorted_frontier):
        print(f"Queue Node {idx}: H: {h}")
        display_state(state, f"Node {idx}:", h_cost=h)

def heuristic_search(start_state):
    start_h = heuristic(start_state)
    frontier = []
    heapq.heappush(frontier, (start_h, start_state, [start_state]))
    explored = set()
    expansion_count = 0

    while frontier:
        print(f"**************************Expansion Step {expansion_count}:**************************")
        display_frontier(frontier)

        h, current_state, path = heapq.heappop(frontier)
        print(f"Expanding Node (H: {h}):")
        display_state(current_state, h_cost=h)

        expansion_count += 1

        if is_goal(current_state):
            print("**************************Goal reached!**************************")
            return path

        explored.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in explored:
                new_h = heuristic(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_h, neighbor, new_path))

    return None

def display_solution_path(solution_path):
    print("Optimal Path (Solution):")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        display_state(state)

if __name__ == "__main__":
    start_state = [
        [1, 0, 3],
        [4, 2, 6],
        [7, 5, 8]
    ]

    display_state(start_state, label="Initial State:")
    print("Starting Greedy Best-First Search...\n")

    solution_path = heuristic_search(start_state)

    if solution_path:
        display_solution_path(solution_path)
    else:
        print("No solution found.")
