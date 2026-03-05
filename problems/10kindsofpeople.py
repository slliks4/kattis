forest1 = [
    ['S', 'T', ''],
    ['', 'T', 'E'],
    ['', '', 'T'],
]

forest2 = [
    ['', 'T', 'E'],
    ['', '', ''],
    ['S', 'T', ''],
    ['', '', ''],
]

start1, end1 = (0, 0), (1, 2)
start2, end2 = (2, 0), (0, 2)


def path_exists(forest, start, end, visited=None):
    # Initialize visited set on first call
    if visited is None:
        visited = set()

    # Get grid dimensions
    rows = len(forest)
    cols = len(forest[0]) if rows > 0 else 0

    # Base case: reached the end
    if start == end:
        return True

    # Check if current position is out of bounds
    row, col = start
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False

    # Check if current position is blocked by tree or already visited
    if forest[row][col] == 'T' or start in visited:
        return False

    # Mark current position as visited
    visited.add(start)

    # Define possible moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Try each direction recursively
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        new_position = (new_row, new_col)

        if path_exists(forest, new_position, end, visited):
            return True

    # Backtrack: remove current position from visited
    visited.remove(start)
    return False
