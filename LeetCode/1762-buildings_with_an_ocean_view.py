"""

https://leetcode.com/problems/buildings-with-an-ocean-view/

There are n buildings in a line. You are given an integer array heights of size n that represents 
the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see 
the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its
right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing 
order.
 

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9

"""

from collections import deque

def findBuildings(heights: list[int]) -> list[int]:
    max_height = 0
    result = deque([])

    for i in reversed(range(len(heights))):
        if heights[i] > max_height:
            max_height = heights[i]
            result.appendleft(i)
    
    return list(result)

if __name__ == "__main__":
    # Test Case 1
    heights = [4,2,3,1]
    print(findBuildings(heights))

    # Test Case 2
    heights = [4,3,2,1]
    print(findBuildings(heights))

    # Test Case 3
    heights = [1,3,2,4]
    print(findBuildings(heights))