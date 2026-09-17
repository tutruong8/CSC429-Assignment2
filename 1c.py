#BFS Grid Implementation using Python
from collections import deque

maze = [
    ['0','1','1','1','1','1'],
    ['0','0','0','0','0','0'],
    ['0','1','1','0','1','1'],
    ['0','1','1','0','1','1'],
    ['0','1','0','0','1','1'],
    ['0','1','0','1','1','1'],
    ['0','0','0','1','1','1']
]

start = (6, 0)
end = (3, 3)

def get_neighbors(grid, cell):
    row, col = cell
    candidates = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    neighbors = []
    
    for r, c in candidates:
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == '0':
                neighbors.append((r, c))
    
    return neighbors

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
        for neighbor in get_neighbors(graph, current):
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

result = bfs(maze, (6, 0), (3, 3))
path = reconstruct_path(result, (6, 0), (3, 3))
print(path)