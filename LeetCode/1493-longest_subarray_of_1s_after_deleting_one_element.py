"""

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the 
resulting array. Return 0 if there is no such subarray.
 

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers 
with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest 
subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

"""

def longestSubarray(nums: list[int]) -> int:
    l = 0
    maxlen = 0
    zeros_left = 1

    for r, num in enumerate(nums):
        zeros_left -= 1 - num

        if zeros_left < 0:
            zeros_left += 1 - nums[l]
            l += 1
        
        maxlen = max(maxlen, r - l)
    
    return maxlen

if __name__ == '__main__':
    # Example 1
    nums1 = [1,1,0,1]
    result1 = longestSubarray(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: 3")

    # Example 2
    nums2 = [0,1,1,1,0,1,1,0,1]
    result2 = longestSubarray(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: 5")

    # Example 3
    nums3 = [1,1,1]
    result3 = longestSubarray(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: 2")