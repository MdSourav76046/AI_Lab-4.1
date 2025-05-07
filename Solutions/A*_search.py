import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    """Compute the Manhattan distance heuristic."""
    mismatch = 0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0 and goal_state[i][j] != state[i][j]:
                mismatch += 1
    return mismatch

def is_goal(state):
    """Check if the current state is the goal state."""
    return state == goal_state

def get_neighbors(state):
    """Return a list of states reachable by sliding a tile into the empty space."""
    neighbors = []
    # Locate the empty tile (represented by 0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j
                break

    # Define possible moves: up, down, left, right.
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in moves:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def display_state(state, label="", f_cost=None, g_cost=None, h_cost=None):
    """Display a 3x3 grid representing the puzzle state."""
    print(f"{label}")
    if f_cost is not None and g_cost is not None and h_cost is not None:
        print(f"  [F: {f_cost}, G: {g_cost}, H: {h_cost}]")

    for row in state:
        print("  " + " ".join(str(tile) if tile != 0 else "*" for tile in row))
    print()

def display_frontier(frontier):
    """Display all nodes currently in the frontier (priority queue)."""
    print("Current Frontier (Queue):")
    sorted_frontier = sorted(frontier, key=lambda x: x[0])  # Sort by F value.
    for idx, (f, g, state, path) in enumerate(sorted_frontier):
        h = f - g  # f = g + h
        print(f"Queue Node {idx}: F: {f}, G: {g}, H: {h}")
        display_state(state, f"Node {idx}:", f, g, h)

def a_star_search(start_state):
    """Perform A* search on the 8-puzzle."""
    start_h = heuristic(start_state)
    frontier = []
    heapq.heappush(frontier, (start_h, 0, start_state, [start_state]))
    explored = set()
    expansion_count = 0

    while frontier:
        # Show all nodes currently in the frontier.
        print(f"**************************Expansion Step {expansion_count}:**************************")
        display_frontier(frontier)

        # Pop the node with the smallest F value.
        f, g, current_state, path = heapq.heappop(frontier)
        h = f - g  # f = g + h

        print(f"Expanding Node (F: {f}, G: {g}, H: {h}):")
        display_state(current_state, f"F: {f}, G: {g}, H: {h}")

        expansion_count += 1

        if is_goal(current_state):
            print("**************************Goal reached!**************************")
            return path

        explored.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in explored:
                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, new_path))

    return None  # No solution found

def display_solution_path(solution_path):
    """Display the optimal solution path step by step."""
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
    print("Starting A* search...\n")

    solution_path = a_star_search(start_state)

    if solution_path:
        display_solution_path(solution_path)
    else:
        print("No solution found.")
