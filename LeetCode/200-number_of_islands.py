"""

https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.
 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

"""

from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and 
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    
    return islands

if __name__ == '__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    print(numIslands(grid))