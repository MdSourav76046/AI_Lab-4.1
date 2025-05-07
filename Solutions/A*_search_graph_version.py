import heapq

# Graph definition: node -> list of (neighbor, cost)
graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

# Heuristic h(n) values
heuristic = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

def a_star_search_verbose(start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], 0, start, [start]))  # (f, g, current_node, path)
    step = 0

    print(f"{'Step':<6}{'Path':<20}{'G(n)':<6}{'H(n)':<6}{'F(n)':<6}")
    print("-" * 50)

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        print(f"{step:<6}{' → '.join(path):<20}{g:<6}{heuristic[current]:<6}{f:<6}")
        step += 1

        if current == goal:
            print(f"\n✅ Goal reached! Final Path: {' → '.join(path)} ; Total cost: {g}")
            return path

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_h = heuristic[neighbor]
            new_f = new_g + new_h
            new_path = path + [neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, new_path))

    print("\n❌ No path found.")
    return None

# Run verbose A* search
a_star_search_verbose('S', 'G')
