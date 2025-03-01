"""

https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum 
number of consecutive 1's in the array if you can flip at most
k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray
is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray
is underlined.
 

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

"""

def longestOnes(nums: list[int], k: int) -> int:
    l, r = 0, 0
    max_ones = 0

    while r < len(nums):
        if nums[r] == 0:
            k -= 1

        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        else:
            max_ones = max(max_ones, r - l + 1)
        
        r += 1
    
    return max_ones


if __name__ == '__main__':
    # Test case 1
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    result = longestOnes(nums, k)
    print(result)
    assert result == 6

    # Test case 2
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    result = longestOnes(nums, k)
    print(result)
    assert result == 10
