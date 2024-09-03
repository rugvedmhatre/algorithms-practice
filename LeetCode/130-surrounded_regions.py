"""

https://leetcode.com/problems/surrounded-regions/

You are given an m x n matrix board containing letters 'X' and
'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or
  vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can 
  connect the region with 'X' cells and none of the region cells
  are on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's 
in the input matrix board. 


Example 1:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because 
it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]


Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

"""

def solve(board: list[list[str]]) -> None:
    rows = len(board)
    cols = len(board[0])

    # Capturing unsurrounded regions
    def capture(r, c):
        if (r < 0 or c < 0 or 
            r == rows or c == cols or 
            board[r][c] != "O"):
            return
        
        board[r][c] = "C"

        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if (board[r][c] == "O" and 
                (r in [0, rows - 1] or
                c in [0, cols - 1])):
                capture(r, c)

    # Capture surrounded regions, and uncapture unsurrounded regions
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "C":
                board[r][c] = "O"

if __name__ == '__main__':
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    solve(board)
    
    for row in board:
        print(row)