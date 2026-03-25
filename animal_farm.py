"""
================================================================================
PROBLEM: C. Animal Farm - Google GSoC 2026
APPROACH: Connected Components using BFS (Breadth-First Search)
COMPLEXITY: Time O(rows * cols), Space O(rows * cols)
================================================================================

PROBLEM STATEMENT:
Given a 2D grid representing a farm where:
- 1 represents a building/wall (obstacle)
- 0 represents open space (room/area)

We need to count the number of distinct rooms (connected components of 0s)
in the farm layout.

SOLUTION LOGIC:
The key insight is that this is a classic "Connected Components" problem
that can be solved using graph traversal (BFS or DFS).

Algorithm:
1. Create a visited matrix to track explored cells
2. Iterate through every cell in the grid
3. When we find an unvisited 0 (open space):
   - Perform BFS to find all connected 0s
   - Mark all connected cells as visited
   - Increment the room counter
4. Return the total room count

Why BFS is strong:
- Guarantees finding all connected cells level by level
- Uses a queue for systematic exploration
- Easy to implement and debug
- Optimal time complexity: O(rows * cols)
================================================================================
"""

from collections import deque
from typing import List, Tuple


class AnimalFarmSolver:
    """
    Senior Developer's Solution for Animal Farm Problem
    Uses BFS to count distinct rooms (connected components of 0s)
    """
    
    def __init__(self, grid: List[List[int]]):
        """
        Initialize the solver with farm grid
        
        Args:
            grid: 2D list where 1=building, 0=open space
        """
        self.grid = grid
        self.rows = len(grid) if grid else 0
        self.cols = len(grid[0]) if grid and len(grid[0]) > 0 else 0
        self.visited = [[False] * self.cols for _ in range(self.rows)]
    
    def is_valid(self, row: int, col: int) -> bool:
        """
        Check if a cell is valid and within grid bounds
        
        Args:
            row: Row index
            col: Column index
            
        Returns:
            True if cell is valid, within bounds, unvisited, and is open space (0)
        """
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                not self.visited[row][col] and 
                self.grid[row][col] == 0)
    
    def bfs(self, start_row: int, start_col: int) -> None:
        """
        Breadth-First Search to explore one complete room
        Marks all connected 0s as visited
        
        Args:
            start_row: Starting row of the room
            start_col: Starting column of the room
        """
        # Initialize queue with starting position
        queue = deque([(start_row, start_col)])
        self.visited[start_row][start_col] = True
        
        # Define 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Process cells level by level
        while queue:
            current_row, current_col = queue.popleft()
            
            # Check all 4 adjacent cells
            for delta_row, delta_col in directions:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
                
                # If adjacent cell is valid, mark it and add to queue
                if self.is_valid(next_row, next_col):
                    self.visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
    
    def count_rooms(self) -> int:
        """
        Count the total number of distinct rooms (connected components)
        
        Algorithm Flow:
        1. Iterate through every cell in grid
        2. Find unvisited open spaces (0s)
        3. For each unvisited 0, run BFS to mark entire room
        4. Count how many BFS traversals we perform (= number of rooms)
        
        Returns:
            Total number of rooms in the farm
        """
        room_count = 0
        
        # Iterate through every cell
        for row in range(self.rows):
            for col in range(self.cols):
                # Found an unvisited open space - this is a new room
                if self.grid[row][col] == 0 and not self.visited[row][col]:
                    # Explore this entire room using BFS
                    self.bfs(row, col)
                    # Increment counter for this new room found
                    room_count += 1
        
        return room_count


def read_input() -> List[List[int]]:
    """
    Read farm grid from standard input
    Format: First line has grid dimensions or grid data
    """
    try:
        # Read number of rows
        line = input().strip()
        rows = int(line)
        
        # Read the grid
        grid = []
        for _ in range(rows):
            row_data = list(map(int, input().strip()))
            grid.append(row_data)
        
        return grid
    except Exception as e:
        print(f"Error reading input: {e}")
        return []


def solve_animal_farm(grid: List[List[int]]) -> int:
    """
    Main solution function - clean interface for solving the problem
    
    Args:
        grid: 2D grid representation of farm
        
    Returns:
        Number of distinct rooms
    """
    if not grid or not grid[0]:
        return 0
    
    solver = AnimalFarmSolver(grid)
    return solver.count_rooms()


# =====================================================================
# EXAMPLE TEST CASES
# =====================================================================

def test_solution():
    """
    Test the solution with example cases from the problem
    """
    print("="*70)
    print("TESTING ANIMAL FARM SOLUTION")
    print("="*70)
    
    # TEST CASE 1: Simple 3x3 grid with middle building
    print("\n[TEST 1] Simple grid with one room:")
    grid1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result1 = solve_animal_farm(grid1)
    print(f"Grid:\n{[row for row in grid1]}")
    print(f"Expected: 1 (all 0s connected)")
    print(f"Result: {result1} rooms")
    print(f"Status: {'✓ PASS' if result1 == 1 else '✗ FAIL'}")
    
    # TEST CASE 2: Grid with two separate rooms
    print("\n[TEST 2] Grid with two separate rooms:")
    grid2 = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    result2 = solve_animal_farm(grid2)
    print(f"Grid:\n{[row for row in grid2]}")
    print(f"Expected: 4 (top-left, top-right, bottom-left, bottom-right)")
    print(f"Result: {result2} rooms")
    print(f"Status: {'✓ PASS' if result2 == 4 else '✗ FAIL'}")
    
    # TEST CASE 3: Complex grid
    print("\n[TEST 3] Complex grid with multiple rooms:")
    grid3 = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0]
    ]
    result3 = solve_animal_farm(grid3)
    print(f"Grid:\n{[row for row in grid3]}")
    print(f"Result: {result3} rooms")
    
    # TEST CASE 4: All building (no rooms)
    print("\n[TEST 4] All buildings (no rooms):")
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result4 = solve_animal_farm(grid4)
    print(f"Grid:\n{[row for row in grid4]}")
    print(f"Expected: 0")
    print(f"Result: {result4} rooms")
    print(f"Status: {'✓ PASS' if result4 == 0 else '✗ FAIL'}")
    
    # TEST CASE 5: All open space (one big room)
    print("\n[TEST 5] All open space (one room):")
    grid5 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result5 = solve_animal_farm(grid5)
    print(f"Grid:\n{[row for row in grid5]}")
    print(f"Expected: 1")
    print(f"Result: {result5} rooms")
    print(f"Status: {'✓ PASS' if result5 == 1 else '✗ FAIL'}")
    
    print("\n" + "="*70)


# =====================================================================
# MAIN EXECUTION
# =====================================================================

if __name__ == "__main__":
    """
    Main entry point - runs test cases to validate the solution
    """
    test_solution()
    
    print("\n[INFO] To solve the actual problem:")
    print("1. Uncomment the following lines:")
    print("   # grid = read_input()")
    print("   # result = solve_animal_farm(grid)")
    print("   # print(result)")
    print("\n2. Provide input in the format:")
    print("   First line: number of rows")
    print("   Following lines: rows of the grid with 0s and 1s")
