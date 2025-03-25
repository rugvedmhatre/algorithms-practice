"""

https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

You are given an integer n representing the dimensions of an n x n grid, with the origin at the 
bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where 
rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. 
Each rectangle is defined as follows:
- (startx, starty): The bottom-left corner of the rectangle.
- (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make 
either two horizontal or two vertical cuts on the grid such that:
- Each of the three resulting sections formed by the cuts contains at least one rectangle.
- Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.

Example 1:
Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
Output: true
Explanation:
The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output 
is true.

Example 2:
Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
Output: true
Explanation:
We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:
Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
Output: false
Explanation:
We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output 
is false.

Constraints:
- 3 <= n <= 10^9
- 3 <= rectangles.length <= 10^5
- 0 <= rectangles[i][0] < rectangles[i][2] <= n
- 0 <= rectangles[i][1] < rectangles[i][3] <= n
- No two rectangles overlap.

"""

def count_non_overlapping(intervals):
    count = 0
    prev_end = -1

    for start, end in intervals:
        if prev_end <= start:
            count += 1
        prev_end = max(prev_end, end)
    return count

def checkValidCuts(n: int, rectangles: list[list[int]]) -> bool:
    x = [(r[0], r[2]) for r in rectangles]
    y = [(r[1], r[3]) for r in rectangles]

    x.sort()
    y.sort()

    return max(
        count_non_overlapping(x),
        count_non_overlapping(y),
    ) >= 3

if __name__ == '__main__':
    # Test Case 1
    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    print(checkValidCuts(n, rectangles))

    # Test Case 2
    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    print(checkValidCuts(n, rectangles))

    # Test Case 3
    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    print(checkValidCuts(n, rectangles))
