#BFS Graph Implementation using Python
from collections import deque

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [], 'F': []
}

def bfs(graph, start, goal):
    frontier = deque([start])
    explored = set()
    came_from = {}

    while frontier:
        current = frontier.popleft()
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

result = bfs(graph, 'A', 'E')
path = reconstruct_path(result, 'A', 'E')
print(path)