"""

https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum 
equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
 

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

"""

def subarraySum(nums: list[int], k: int) -> int:
    result = 0
    current_sum = 0
    prefix_sums = {0:1}

    for n in nums:
        current_sum += n
        difference = current_sum - k
        result += prefix_sums.get(difference, 0)

        prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
    
    return result

if __name__ == "__main__":
    # Test Case 1
    nums = [1,1,1]
    k = 2
    print(subarraySum(nums, k))

    # Test Case 2
    nums = [1,2,3]
    k = 3
    print(subarraySum(nums, k))