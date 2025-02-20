"""

https://leetcode.com/problems/shortest-bridge/

You are given an n x n binary matrix grid where 1 represents 
land and 0 represents water.

An island is a 4-directionally connected group of 1's not 
connected to any other 1's. There are exactly two islands in 
grid.

You may change 0's to 1's to connect the two islands to form 
one island.

Return the smallest number of 0's you must flip to connect 
the two islands.


Example 1:
Input: grid = [[0,1],
               [1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],
               [0,0,0],
               [0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,1,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]]
Output: 1
 

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 100
- grid[i][j] is either 0 or 1.
- There are exactly two islands in grid.

"""

from collections import deque

def shortestBridge(grid: list[list[int]]) -> int:
    N = len(grid)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def invalid(r, c):
        return r < 0 or c < 0 or r == N or c == N

    visited = set()

    def dfs(r, c):
        if (invalid(r, c) or not grid[r][c] or (r, c) in visited):
            return
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    def bfs():
        result = 0
        queue = deque(visited)

        while queue:
            q_len = len(queue)
            for i in range(q_len):
                r, c = queue.popleft()
                for dr, dc in directions:
                    curR, curC = r + dr, c + dc
                    if invalid(curR, curC) or (curR, curC) in visited:
                        continue
                    if grid[curR][curC]:
                        return result
                    queue.append((curR, curC))
                    visited.add((curR, curC))
            result += 1

    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                dfs(r, c)
                return bfs()
            
if __name__ == "__main__":
    grid = [[0,1],
            [1,0]]
    print(shortestBridge(grid))  # 1

    grid = [[0,1,0],
            [0,0,0],
            [0,0,1]]
    print(shortestBridge(grid))  # 2

    grid = [[1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]]
    print(shortestBridge(grid))  # 1