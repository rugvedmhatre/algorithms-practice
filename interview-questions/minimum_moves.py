"""

There is a maze in HackerPlay where children play for recreation. 

The maze is represented as an (n*m) grid of cells, where each cell
is either empty (denoted by 0) or contains an obstacle (denoted 
by 1). HackerMan is currently standing at cell (0, 0) and wishes
to reach the cell (n-1, m-1).

For a jump parameter denoted by k, in one move, HackerMan can move
to any of the following cells:
- (i + x, j) where 1 <= x <= k, provided cell (i + x, j) lies in
  the maze and there are no cells containing obstacles in the 
  range(i, j) -> (i+1, j) … -> (i+x, j)
- (i, j + x) where 1 <= x <= k, provided cell (i, j + x) lies in
  the maze and there are no cells containing obstacles in the 
  range(i, j) -> (i, j+1) … -> (i, j + x)
- (i - x, j) where 1 <= x <= k, provided cell (i - x, j) lies in
  the maze and there are no cells containing obstacles in the
  range(i, j) -> (i-1, j) … -> (i-x, j)
- (i, j - x) where 1 <= x <= k, provided cell (i, j - x) lies in
  the maze and there are no cells containing obstacles in the
  range(i, j) -> (i, j-1) … -> (i, j - x)

Find the minimum number of moves in which HackerMan can reach the
cell (n-1, m-1) starting from (0, 0) or -1 if it is impossible to
reach that cell.

"""

from collections import deque

def minimum_moves(maze, k):
    n, m = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    
    # Start BFS from (0, 0)
    queue = deque([(0, 0, 0)])  # (row, col, moves)
    visited[0][0] = True
    
    while queue:
        i, j, moves = queue.popleft()
        
        # If we have reached the bottom-right corner
        if i == n - 1 and j == m - 1:
            return moves
        
        # Explore all four directions
        for di, dj in directions:
            for x in range(1, k + 1):
                ni, nj = i + di * x, j + dj * x
                
                # Check bounds
                if 0 <= ni < n and 0 <= nj < m:
                    # Ensure path is clear of obstacles
                    clear_path = True
                    for step in range(1, x + 1):
                        if maze[i + di * step][j + dj * step] == 1:
                            clear_path = False
                            break
                    
                    if clear_path and not visited[ni][nj]:
                        visited[ni][nj] = True
                        queue.append((ni, nj, moves + 1))
                else:
                    break

    # If the target was not reached
    return -1

def testCase0():
    maze = [
        [0, 0],
        [1, 0],
    ]
    k = 2
    result = minimum_moves(maze, k)
    print(result)
    assert(result == 2)

def testCase1():
    maze = [
        [0, 0, 0],
        [1, 0, 0],
    ]
    k = 5
    result = minimum_moves(maze, k)
    print(result)
    assert(result == 2)

def testCase2():
    maze = [
        [0, 1, 0],
        [1, 0, 0],
    ]
    k = 5
    result = minimum_moves(maze, k)
    print(result)
    assert(result == -1)

if __name__ == '__main__':
    testCase0()
    testCase1()
    testCase2()
