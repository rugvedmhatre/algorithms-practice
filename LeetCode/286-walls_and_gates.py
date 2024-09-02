"""

https://neetcode.io/problems/islands-and-treasure/

You are given a m * n 2D grid initialized with these three 
possible values:
- -1 - A water cell that can not be traversed.
- 0 - A treasure chest.
- INF - A land cell that can be traversed. We use the integer
  2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure
chest. If a land cell cannot reach a treasure chest than the
value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]
Output: [
  [0,-1],
  [1,2]
]


Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is one of {-1, 0, 2147483647}

"""

from collections import deque

def islandsAndTreasure(grid: list[list[int]]) -> None:
    rows = len(grid)
    cols = len(grid[0])
    
    visited = set()

    q = deque()

    def addRoom(r, c):
        if (r < 0 or r == rows or
            c < 0 or c == cols or
            (r, c) in visited or
            grid[r][c] == -1):
            return
        
        visited.add((r, c))
        q.append((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))
    
    distance = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = distance
            for dr, dc in directions:
                addRoom(r + dr, c + dc)
        distance += 1

if __name__ == '__main__':
    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    
    islandsAndTreasure(grid)

    for i in range(len(grid)):
        print(grid[i])