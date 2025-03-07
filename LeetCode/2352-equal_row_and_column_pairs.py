"""

https://leetcode.com/problems/equal-row-and-column-pairs/

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri 
and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order 
(i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5

"""

from collections import defaultdict

def equalPairs(grid: list[list[int]]) -> int:
    pairs = defaultdict(int)
    total_pairs = 0
    n = len(grid)

    for c in range(n):
        column = []
        for r in range(n):
            column.append(grid[r][c])
        pairs[tuple(column)] += 1
    
    for r in range(n):
        row = tuple(grid[r][:])
        total_pairs += pairs[row]
    
    return total_pairs

if __name__ == '__main__':
    # Test Case 1
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print(equalPairs(grid))

    # Test Case 2
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(grid))
