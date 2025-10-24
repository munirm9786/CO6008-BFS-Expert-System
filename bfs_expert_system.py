# CO6008 Knowledge-Based Systems Coursework 
# Expert System: Pathfinding using Breadth-First Search
# Munir Mohammed


from collections import deque

# KNOWLEDGE BASE 
# The graph stores all possible connections between nodes.
# Each line acts like a rule, for example, "IF at A THEN can go to B or C".
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['F', 'H'],
    'F': ['I'],
    'G': [],
    'H': ['I'],
    'I': []
}

#  INFERENCE ENGINE
# The BFS algorithm is the reasoning part of this expert system.
# It searches all possible paths level by level until it finds the goal.
def bfs_path(graph, start, goal):
    queue = deque([[start]])   # Queue stores paths
    visited = set()            # Keeps track of visited nodes

    while queue:
        path = queue.popleft()  # Get the first path in the queue
        node = path[-1]         # Get the last node in the current path

        if node == goal:
            return path  # Found the goal, return the full path

        if node not in visited:
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

    return None  # No path found


#  USER INTERFACE 
print("=== PATHFINDING EXPERT SYSTEM ===")
start = input("Enter start node (e.g., A): ").upper()
goal = input("Enter goal node (e.g., I): ").upper()

# INFERENCE EXECUTION
path = bfs_path(graph, start, goal)

#  OUTPUT SECTION
if path:
    print("\n✅ Shortest path found:")
    print(" → ".join(path))
else:
    print("\n❌ No path found between the given nodes.")
