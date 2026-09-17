#DFS Graph Implementation using Python

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [], 'F': []
}

def dfs(graph, start, goal):
    frontier = [start]
    explored = set()
    came_from = {}

    while frontier:
        current = frontier.pop()
        print("visiting:", current)
        if current == goal:
            return came_from
        explored.add(current)
        for neighbor in graph[current]:
            if neighbor not in explored and neighbor not in frontier:
                came_from[neighbor] = current
                frontier.append(neighbor)
    return None

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

result = dfs(graph, 'A', 'E')
path = reconstruct_path(result, 'A', 'E')
print(path)