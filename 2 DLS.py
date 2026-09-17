#DLS Grid Implementation using Python
from collections import deque
from matplotlib.pyplot import grid

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

def dls(graph, start, goal, limit):
    frontier = [(start, 0)]
    explored = set()
    came_from = {}
    current_depth = 0

    while frontier:
        current, current_depth = frontier.pop()
        print("visiting:", current)
        if current == goal:
            return came_from
        explored.add(current)
        if current_depth < limit:
            for neighbor in get_neighbors(graph, current):
                    if neighbor not in explored and neighbor not in [n for n, d in frontier]:
                        came_from[neighbor] = current
                        frontier.append((neighbor, current_depth + 1))
    return None

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

#limit = 6
result = dls(maze, (6, 0), (3, 3), limit=6)
if result is not None:
    path = reconstruct_path(result, (6, 0), (3, 3))
    print(path)
else:
    print("No path found within limit = 6")

#limit = 10
result2 = dls(maze, (6, 0), (3, 3), limit=10)
if result2 is not None:
    path2 = reconstruct_path(result2, (6, 0), (3, 3))
    print(path2)
else:
    print("No path found within limit = 10")


#limit = 5
result3 = dls(maze, (6, 0), (3, 3), limit=5)
if result3 is not None:
    path3 = reconstruct_path(result3, (6, 0), (3, 3))
    print(path3)
else:
    print("No path found within limit = 5")