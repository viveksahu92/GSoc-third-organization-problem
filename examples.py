"""
QUICK START GUIDE - Animal Farm Solution
========================================

This file shows you exactly how to use the solution
"""

from animal_farm import solve_animal_farm, AnimalFarmSolver


# ==========================================
# EXAMPLE 1: Using the Simple Function
# ==========================================
def example_1_simple_usage():
    """Simplest way to solve the problem"""
    print("EXAMPLE 1: Simple Usage")
    print("-" * 50)
    
    # Your farm grid (0 = open space, 1 = building)
    farm = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    
    # Solve in one line!
    result = solve_animal_farm(farm)
    
    print(f"Farm grid:\n{farm}")
    print(f"\nNumber of rooms: {result}")
    print()


# ==========================================
# EXAMPLE 2: Using the Class (More Control)
# ==========================================
def example_2_class_usage():
    """More detailed way with the class"""
    print("EXAMPLE 2: Class Usage")
    print("-" * 50)
    
    farm = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    # Create solver object
    solver = AnimalFarmSolver(farm)
    
    # Get the result
    result = solver.count_rooms()
    
    print(f"Farm grid:\n{farm}")
    print(f"Grid dimensions: {solver.rows} rows × {solver.cols} columns")
    print(f"Number of rooms: {result}")
    print()


# ==========================================
# EXAMPLE 3: Reading from Input
# ==========================================
def example_3_reading_input():
    """
    When you get input from OmegaUp or online judge:
    
    Input format:
    3
    0 0 1
    0 1 0
    1 0 0
    """
    print("EXAMPLE 3: Reading from Input")
    print("-" * 50)
    
    # Simulate reading input
    input_data = """3
0 0 1
0 1 0
1 0 0"""
    
    lines = input_data.strip().split('\n')
    
    # Parse the input
    n = int(lines[0])  # number of rows
    farm = []
    
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        farm.append(row)
    
    # Solve
    result = solve_animal_farm(farm)
    
    print(f"Read {n} rows from input")
    print(f"Farm grid:\n{farm}")
    print(f"Answer: {result}")
    print()


# ==========================================
# EXAMPLE 4: Real-World Scenario
# ==========================================
def example_4_real_scenario():
    """A real farming scenario"""
    print("EXAMPLE 4: Real Farm Scenario")
    print("-" * 50)
    
    # A complex farm layout
    farm = [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    
    result = solve_animal_farm(farm)
    
    print(f"Complex farm layout:")
    for i, row in enumerate(farm):
        print(f"  Row {i}: {row}")
    print(f"\nTotal distinct rooms for animals: {result}")
    print()


# ==========================================
# EXAMPLE 5: Edge Cases
# ==========================================
def example_5_edge_cases():
    """Test edge cases"""
    print("EXAMPLE 5: Edge Cases")
    print("-" * 50)
    
    # Case 1: No rooms (all buildings)
    print("\n1. All buildings (no space for animals):")
    farm1 = [[1, 1], [1, 1]]
    print(f"   Grid: {farm1}")
    print(f"   Rooms: {solve_animal_farm(farm1)}")
    
    # Case 2: One big room
    print("\n2. One big room (all open):")
    farm2 = [[0, 0], [0, 0]]
    print(f"   Grid: {farm2}")
    print(f"   Rooms: {solve_animal_farm(farm2)}")
    
    # Case 3: Single cell
    print("\n3. Single cell (open):")
    farm3 = [[0]]
    print(f"   Grid: {farm3}")
    print(f"   Rooms: {solve_animal_farm(farm3)}")
    
    # Case 4: Single building
    print("\n4. Single building:")
    farm4 = [[1]]
    print(f"   Grid: {farm4}")
    print(f"   Rooms: {solve_animal_farm(farm4)}")
    print()


# ==========================================
# MAIN - RUN ALL EXAMPLES
# ==========================================
if __name__ == "__main__":
    print("="*50)
    print("ANIMAL FARM SOLUTION - QUICK START EXAMPLES")
    print("="*50)
    print()
    
    example_1_simple_usage()
    example_2_class_usage()
    example_3_reading_input()
    example_4_real_scenario()
    example_5_edge_cases()
    
    print("="*50)
    print("✓ All examples completed successfully!")
    print("="*50)
