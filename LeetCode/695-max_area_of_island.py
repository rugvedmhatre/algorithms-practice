"""

https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group
of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in 
the island.

Return the maximum area of an island in grid. If there is no 
island, return 0.
 

Example 1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be 
connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

"""

from collections import deque

# Using BFS
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    maxArea = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        currentArea = 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == 1 and
                    (r, c) not in visited):
                    q.append((r, c))
                    visited.add((r, c))
                    currentArea += 1
        
        return currentArea
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                maxArea = max(maxArea, bfs(r, c))
    
    return maxArea

# Using DFS
def maxAreaOfIsland(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    maxArea = 0

    def dfs(r, c):
        if (r not in range(rows) or 
            c not in range(cols) or 
            grid[r][c] == 0 or 
            (r, c) in visited):
            return 0
        
        visited.add((r, c))
        
        return (1 + dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                maxArea = max(maxArea, dfs(r, c))
    
    return maxArea

if __name__ == '__main__':
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

    print(maxAreaOfIsland(grid))