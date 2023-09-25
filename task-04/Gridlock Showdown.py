def check_winner(grid, symbol):
    
    for row in grid:
        if all(cell == symbol for cell in row):
            return True
    
    
    for col in range(3):
        if all(grid[row][col] == symbol for row in range(3)):
            return True
    
    
    if all(grid[i][i] == symbol for i in range(3)) or all(grid[i][2 - i] == symbol for i in range(3)):
        return True
    
    return False

def determine_winner(grid):
    if check_winner(grid, "X"):
        return "X"
    elif check_winner(grid, "O"):
        return "O"
    elif check_winner(grid, "+"):
        return "+"
    else:
        return "DRAW"

def main():
    t = int(input("Enter number of test cases (1 ≤ t ≤ 10000): "))
    
    if t < 1 or t > 10000:
        print("Invalid number of test cases.")
        return
    
    for _ in range(t):
        print("Enter the grid for test case:")
        grid = [list(input().strip()) for _ in range(3)]
        
        result = determine_winner(grid)
        print("Result:", result)

if __name__ == "__main__":
    main()
