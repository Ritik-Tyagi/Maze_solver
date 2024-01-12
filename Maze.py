import random
def generate_maze(rows, cols, start, end):
    maze = [["🟥"] * cols for _ in range(rows)]
    stack = [(0, 0)]
    visited = set()

    while stack:
        current = stack[-1]
        x, y = current

        maze[x][y] = "🟦" # Mark the current cell as visited

        if current == end:
            break

        neighbors = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()

    return maze