from collections import deque

def solve():
    """
    Animal Farm Problem - Count distinct areas in buildings
    
    Each cell has walls encoded as 0-15:
    - Bit 0 (1): Top wall
    - Bit 1 (2): Right wall
    - Bit 2 (4): Bottom wall
    - Bit 3 (8): Left wall
    
    Two cells are connected if no wall separates them.
    """
    
    # Read number of buildings
    t = int(input())
    
    for _ in range(t):
        # Read building dimensions
        x, y = map(int, input().split())
        
        # Read the grid
        grid = []
        for i in range(y):
            row = list(map(int, input().split()))
            grid.append(row)
        
        # Count areas in this building
        areas = count_areas(grid, y, x)
        print(areas)


def count_areas(grid, rows, cols):
    """
    Count number of distinct areas in building
    
    Key: Cells on edges that open to outside should be connected to virtual "outside" area
    """
    # Track visited cells
    visited = [[False] * cols for _ in range(rows)]
    area_count = 0
    
    # First, do BFS from a virtual "outside" node
    # Connect all edge cells that are open to outside
    bfs_outside_area(grid, visited, rows, cols)
    
    # Now count remaining connected regions
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Start BFS from this unvisited cell
                bfs_explore(grid, visited, r, c, rows, cols)
                area_count += 1
    
    # +1 for the outside area (if any cell opens to outside)
    if any(visited[r][c] for r in range(rows) for c in range(cols) if is_edge_open(grid, r, c, rows, cols)):
        area_count += 1
    
    return area_count


def is_edge_open(grid, r, c, rows, cols):
    """Check if this edge cell is open to outside"""
    walls = grid[r][c]
    
    # Check if on edge and open in that direction
    if r == 0 and not (walls & 1):  # Top edge, no top wall
        return True
    if r == rows-1 and not (walls & 4):  # Bottom edge, no bottom wall
        return True
    if c == 0 and not (walls & 8):  # Left edge, no left wall
        return True
    if c == cols-1 and not (walls & 2):  # Right edge, no right wall
        return True
    
    return False


def bfs_outside_area(grid, visited, rows, cols):
    """
    BFS from virtual outside node to mark all cells connected to outside
    """
    queue = deque()
    
    # Add all edge cells that are open to outside
    for r in range(rows):
        for c in range(cols):
            if is_edge_open(grid, r, c, rows, cols):
                if not visited[r][c]:
                    queue.append((r, c))
                    visited[r][c] = True
    
    # BFS to find all cells connected to outside
    while queue:
        r, c = queue.popleft()
        walls = grid[r][c]
        
        # TOP
        if not (walls & 1) and r > 0 and not visited[r-1][c]:
            upper_walls = grid[r-1][c]
            if not (upper_walls & 4):
                visited[r-1][c] = True
                queue.append((r-1, c))
        
        # RIGHT
        if not (walls & 2) and c < cols-1 and not visited[r][c+1]:
            right_walls = grid[r][c+1]
            if not (right_walls & 8):
                visited[r][c+1] = True
                queue.append((r, c+1))
        
        # BOTTOM
        if not (walls & 4) and r < rows-1 and not visited[r+1][c]:
            lower_walls = grid[r+1][c]
            if not (lower_walls & 1):
                visited[r+1][c] = True
                queue.append((r+1, c))
        
        # LEFT
        if not (walls & 8) and c > 0 and not visited[r][c-1]:
            left_walls = grid[r][c-1]
            if not (left_walls & 2):
                visited[r][c-1] = True
                queue.append((r, c-1))


def bfs_explore(grid, visited, start_r, start_c, rows, cols):
    """
    BFS to mark all connected cells as visited
    Two cells are connected if there's no wall between them
    
    Wall encoding:
    - Bit 0 (value 1): Top wall
    - Bit 1 (value 2): Right wall
    - Bit 2 (value 4): Bottom wall
    - Bit 3 (value 8): Left wall
    
    For connection between cells:
    - Current cell must NOT have wall in that direction
    - Adjacent cell must NOT have wall on the opposite side
    """
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        walls = grid[r][c]
        
        # Check all 4 directions
        
        # TOP: Current cell no top wall (bit 0) AND upper cell no bottom wall (bit 2)
        if not (walls & 1) and r > 0 and not visited[r-1][c]:
            upper_walls = grid[r-1][c]
            if not (upper_walls & 4):  # Upper cell has no bottom wall
                visited[r-1][c] = True
                queue.append((r-1, c))
        
        # RIGHT: Current cell no right wall (bit 1) AND right cell no left wall (bit 3)
        if not (walls & 2) and c < cols-1 and not visited[r][c+1]:
            right_walls = grid[r][c+1]
            if not (right_walls & 8):  # Right cell has no left wall
                visited[r][c+1] = True
                queue.append((r, c+1))
        
        # BOTTOM: Current cell no bottom wall (bit 2) AND lower cell no top wall (bit 0)
        if not (walls & 4) and r < rows-1 and not visited[r+1][c]:
            lower_walls = grid[r+1][c]
            if not (lower_walls & 1):  # Lower cell has no top wall
                visited[r+1][c] = True
                queue.append((r+1, c))
        
        # LEFT: Current cell no left wall (bit 3) AND left cell no right wall (bit 1)
        if not (walls & 8) and c > 0 and not visited[r][c-1]:
            left_walls = grid[r][c-1]
            if not (left_walls & 2):  # Left cell has no right wall
                visited[r][c-1] = True
                queue.append((r, c-1))


if __name__ == "__main__":
    solve()
