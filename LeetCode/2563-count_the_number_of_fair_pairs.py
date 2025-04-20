"""

https://leetcode.com/problems/count-the-number-of-fair-pairs/

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number 
of fair pairs.

A pair (i, j) is fair if:
- 0 <= i < j < n, and
- lower <= nums[i] + nums[j] <= upper
 

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:
- 1 <= nums.length <= 10^5
- nums.length == n
- -10^9 <= nums[i] <= 10^9
- -10^9 <= lower <= upper <= 10^9

"""

def countFairPairs(nums: list[int], lower: int, upper: int) -> int:
    def binarySearch(l, r, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return r
    
    nums.sort()
    result = 0

    for i in range(len(nums)):
        low = lower - nums[i]
        up = upper - nums[i]
        result += (
            binarySearch(i+1, len(nums)-1, up+1) - 
            binarySearch(i+1, len(nums)-1, low)
        )
    
    return result

if __name__ == "__main__":
    # Test Case 1
    nums = [0,1,7,4,4,5]
    lower = 3
    upper = 6
    print(countFairPairs(nums, lower, upper))

    # Test Case 2
    nums = [1,7,9,2,5]
    lower = 11
    upper = 11
    print(countFairPairs(nums, lower, upper))