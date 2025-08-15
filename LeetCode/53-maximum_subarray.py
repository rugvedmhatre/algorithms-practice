"""

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide 
and conquer approach, which is more subtle.

"""

def maxSubArray(nums: list[int]) -> int:
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    
    return maxSub

if __name__ == "__main__":
    # Test Case 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

    # Test Case 2
    nums = [1]
    print(maxSubArray(nums))

    # Test Case 3
    nums = [5,4,-1,7,8]
    print(maxSubArray(nums))