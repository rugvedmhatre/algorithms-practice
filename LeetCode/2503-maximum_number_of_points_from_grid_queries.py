"""

https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell
of the matrix and repeat the following process:

- If queries[i] is strictly greater than the value of the current cell that you are in, then you 
  get one point if it is your first time visiting this cell, and you can move to any adjacent cell 
  in all 4 directions: up, down, left, and right.
- Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note that for each query 
you are allowed to visit the same cell multiple times.

Return the resulting array answer.

Example 1:
Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:
Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater 
than or equal to 3.


Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 1000
- 4 <= m * n <= 10^5
- k == queries.length
- 1 <= k <= 10^4
- 1 <= grid[i][j], queries[i] <= 10^6

"""

from queue import PriorityQueue

def maxPoints(grid: list[list[int]], queries: list[int]) -> list[int]:
    rows, cols = len(grid), len(grid[0])
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
    result = [0] * len(queries)
    
    heap = PriorityQueue()
    visited = [[False] * cols for _ in range(rows)]
    
    heap.put((grid[0][0], 0, 0))
    visited[0][0] = True
    points = 0
    
    for query_val, query_idx in sorted_queries:
        while not heap.empty() and heap.queue[0][0] < query_val:
            _, row, col = heap.get()
            points += 1
            
            for dr, dc in DIRECTIONS:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    not visited[nr][nc]):
                    heap.put((grid[nr][nc], nr, nc))
                    visited[nr][nc] = True
        
        result[query_idx] = points
    
    return result

if __name__ == '__main__':
    # Test Case 1
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    print(maxPoints(grid, queries))

    # Test Case 2
    grid = [[5,2,1],[1,1,2]]
    queries = [3]
    print(maxPoints(grid, queries))