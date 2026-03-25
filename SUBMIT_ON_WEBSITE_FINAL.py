from collections import deque

# Official encoding from the statement image:
# values 0..15 are NOT direct bitmasks.
# We convert them to a bitmask where:
# 1=top wall, 2=right wall, 4=bottom wall, 8=left wall.
VALUE_TO_WALLS = {
    0: 0,
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 1 | 2,
    6: 1 | 4,
    7: 1 | 8,
    8: 2 | 4,
    9: 2 | 8,
    10: 4 | 8,
    11: 1 | 2 | 4,
    12: 1 | 2 | 8,
    13: 1 | 4 | 8,
    14: 2 | 4 | 8,
    15: 1 | 2 | 4 | 8,
}


def is_open_to_outside(cell_walls, r, c, rows, cols):
    if r == 0 and (cell_walls & 1) == 0:
        return True
    if c == cols - 1 and (cell_walls & 2) == 0:
        return True
    if r == rows - 1 and (cell_walls & 4) == 0:
        return True
    if c == 0 and (cell_walls & 8) == 0:
        return True
    return False


def bfs_region(grid, visited, sr, sc, rows, cols):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    touches_outside = is_open_to_outside(grid[sr][sc], sr, sc, rows, cols)

    while q:
        r, c = q.popleft()
        w = grid[r][c]

        # Up
        if r > 0 and not visited[r - 1][c]:
            if (w & 1) == 0 and (grid[r - 1][c] & 4) == 0:
                visited[r - 1][c] = True
                q.append((r - 1, c))
                if is_open_to_outside(grid[r - 1][c], r - 1, c, rows, cols):
                    touches_outside = True

        # Right
        if c < cols - 1 and not visited[r][c + 1]:
            if (w & 2) == 0 and (grid[r][c + 1] & 8) == 0:
                visited[r][c + 1] = True
                q.append((r, c + 1))
                if is_open_to_outside(grid[r][c + 1], r, c + 1, rows, cols):
                    touches_outside = True

        # Down
        if r < rows - 1 and not visited[r + 1][c]:
            if (w & 4) == 0 and (grid[r + 1][c] & 1) == 0:
                visited[r + 1][c] = True
                q.append((r + 1, c))
                if is_open_to_outside(grid[r + 1][c], r + 1, c, rows, cols):
                    touches_outside = True

        # Left
        if c > 0 and not visited[r][c - 1]:
            if (w & 8) == 0 and (grid[r][c - 1] & 2) == 0:
                visited[r][c - 1] = True
                q.append((r, c - 1))
                if is_open_to_outside(grid[r][c - 1], r, c - 1, rows, cols):
                    touches_outside = True

    return touches_outside


def count_areas(raw_grid, rows, cols):
    # Decode statement values to actual wall bitmask.
    grid = [[VALUE_TO_WALLS[v] for v in row] for row in raw_grid]

    visited = [[False] * cols for _ in range(rows)]
    interior_regions = 0
    has_outside_region = False

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                touches_outside = bfs_region(grid, visited, r, c, rows, cols)
                if touches_outside:
                    has_outside_region = True
                else:
                    interior_regions += 1

    return interior_regions + (1 if has_outside_region else 0)


def solve():
    t = int(input().strip())
    for _ in range(t):
        x, y = map(int, input().split())
        raw_grid = [list(map(int, input().split())) for _ in range(y)]
        print(count_areas(raw_grid, y, x))


if __name__ == "__main__":
    solve()
