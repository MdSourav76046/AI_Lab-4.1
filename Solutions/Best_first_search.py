import heapq

# Graph as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': ['H'],
    'F': ['I', 'G'],
    'H': [],
    'I': [],
    'G': []
}

# Heuristic values for each node (h(n))
heuristics = {
    'S': 14,
    'A': 12,
    'B': 5,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'H': 4,
    'I': 9,
    'G': 0
}

def best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start, [start]))  # (h(n), node, path)
    closed_list = set()

    print("Initialization:")
    print(f"Open: {[start]}, Closed: []\n")

    while open_list:
        h, current, path = heapq.heappop(open_list)
        print(f"Expanding: {current}")
        closed_list.add(current)

        if current == goal:
            print(f"\nGoal found! Final path: {' → '.join(path)}")
            return path

        for neighbor in graph[current]:
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor, path + [neighbor]))

        open_nodes = [node for _, node, _ in sorted(open_list)]
        print(f"Open: {open_nodes}, Closed: {list(closed_list)}\n")

    print("Goal not found.")
    return None

# Run the algorithm
best_first_search('S', 'D')
