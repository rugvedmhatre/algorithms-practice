"""

https://leetcode.com/problems/split-array-largest-sum/

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the 
largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
 

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays 
is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays 
is only 9.
 

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= k <= min(50, nums.length)

"""

def splitArray(nums: list[int], k: int) -> int:
    l = max(nums)
    r = sum(nums)
    result = 0

    def minsubarrays(mid):
        cur_sum = 0
        splits = 1
        
        for n in nums:
            if cur_sum + n <= mid:
                cur_sum += n
            else:
                cur_sum = n
                splits += 1
        
        return splits

    while l <= r:
        mid = (l + r) // 2

        if minsubarrays(mid) <= k:
            r = mid - 1
            result = mid
        else:
            l = mid + 1
    
    return result

if __name__ == "__main__":
    # Test Case 1
    nums = [7,2,5,10,8]
    k = 2
    print(splitArray(nums, k))

    # Test Case 2
    nums = [1,2,3,4,5]
    k = 2
    print(splitArray(nums, k))