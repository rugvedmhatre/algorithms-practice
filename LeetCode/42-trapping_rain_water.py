"""

https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap 
after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented 
by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain 
water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

"""

# # Method 1: O(n) time | O(n) space
# def trap(height: list[int]) -> int:
#     currentMax = 0
#     maxLeft = []
#     for i in range(len(height)):
#         currentMax = max(currentMax, height[i])
#         maxLeft.append(currentMax)
    
#     currentMax = 0
#     maxRight = []
#     for i in range(len(height) - 1, -1, -1):
#         currentMax = max(currentMax, height[i])
#         maxRight.append(currentMax)

#     maxRight = maxRight[::-1]
    
#     waterStored = 0

#     for i in range(len(height)):
#         waterStored += max(0, min(maxLeft[i], maxRight[i]) - height[i])
    
#     return waterStored

# Method 2: O(n) time | O(1) space
def trap(height: list[int]) -> int:
        
    if len(height) == 0:
        return 0

    left = 0
    right = len(height) - 1

    maxLeft = height[left]
    maxRight = height[right]

    waterStored = 0

    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            waterStored += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            waterStored += maxRight - height[right]
    
    return waterStored

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))