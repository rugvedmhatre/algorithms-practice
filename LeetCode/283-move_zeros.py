"""
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

"""

def moveZeros(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print("Input  :", nums)
    moveZeros(nums)
    print("Result :", nums)