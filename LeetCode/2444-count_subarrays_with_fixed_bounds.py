"""

https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
- The minimum value in the subarray is equal to minK.
- The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i], minK, maxK <= 10^6

"""

def countSubarrays(nums: list[int], minK: int, maxK: int) -> int:
    pMin = pMax = bad = -1
    ans = 0
    
    for i, num in enumerate(nums):
        if num == minK:
            pMin = i
        if num == maxK:
            pMax = i
        if num < minK or num > maxK:
            bad = i
        if pMin != -1 and pMax != -1:
            ans += max(0, min(pMin, pMax) - bad)
    
    return ans

if __name__ == "__main__":
    # Test Case 1
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    print(countSubarrays(nums, minK, maxK))

    # Test Case 2
    nums = [1,1,1,1]
    minK = 1
    maxK = 1
    print(countSubarrays(nums, minK, maxK))