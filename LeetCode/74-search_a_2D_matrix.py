"""

https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following 
two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer 
  of the previous row.

Given an integer target, return true if target is in matrix or 
false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

"""

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        # print(row, col, matrix[row][col])
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    
    return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))