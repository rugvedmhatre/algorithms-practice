"""

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to
or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return
-1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10^5
- 1 <= m * n <= 10^5
- 1 <= x, grid[i][j] <= 10^4

"""

def minOperations(grid: list[list[int]], x: int) -> int:
    total = 0
    nums = []
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            total += grid[r][c]
            nums.append(grid[r][c])
            if (grid[r][c] % x) != (grid[0][0] % x):
                return -1
    
    nums.sort()

    prefix_sum = 0
    result = float('inf')

    for i, n in enumerate(nums):
        cost_left = n * i - prefix_sum
        cost_right = total - prefix_sum - (n * (len(nums) - i))
        operations = (cost_left + cost_right) // x
        result = min(result, operations)
        prefix_sum += n
    
    return result

if __name__ == '__main__':
    # Test Case 1
    grid = [[2,4],[6,8]]
    x = 2
    print(minOperations(grid, x))

    # Test Case 2
    grid = [[1,5],[2,3]]
    x = 1
    print(minOperations(grid, x))

    # Test Case 3
    grid = [[1,2],[3,4]]
    x = 2
    print(minOperations(grid, x))
