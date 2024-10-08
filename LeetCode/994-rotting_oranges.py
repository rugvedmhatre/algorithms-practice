"""

https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of 
three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no 
cell has a fresh orange. If this is impossible, return -1.
 

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, 
column 0) is never rotten, because rotting only happens 
4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at 
minute 0, the answer is just 0. 


Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

"""

from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    time = 0
    fresh = 0

    rows = len(grid)
    cols = len(grid[0])

    q = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append((r, c))
    
    if fresh == 0:
        return 0
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row in range(rows) and 
                    col in range(cols) and 
                    grid[row][col] == 1
                ):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1
    
    return time if fresh == 0 else -1

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))