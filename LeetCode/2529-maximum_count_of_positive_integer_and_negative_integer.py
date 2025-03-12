"""

https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

Given an array nums sorted in non-decreasing order, return the maximum between the number of 
positive integers and the number of negative integers.

- In other words, if the number of positive integers in nums is pos and the number of negative
  integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.


Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them 
is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them
is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them
is 4.


Constraints:
- 1 <= nums.length <= 2000
- -2000 <= nums[i] <= 2000
- nums is sorted in a non-decreasing order.

Follow up: Can you solve the problem in O(log(n)) time complexity?

"""

def maximumCount(nums: list[int]) -> int:
    if nums[0] == 0 and nums[-1] == 0:
        return 0

    if nums[0] > 0 or nums[-1] < 0:
        return len(nums)

    neg_count = binary_search(nums, 0)
    pos_count = len(nums) - binary_search(nums, 1)
    return max(neg_count, pos_count)
    
def binary_search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    result = len(nums)

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            result = mid
            r = mid - 1

    return result


if __name__ == '__main__':
    # Test Case 1
    nums = [-2,-1,-1,1,2,3]
    print(maximumCount(nums))

    # Test Case 2
    nums = [-3,-2,-1,0,0,1,2]
    print(maximumCount(nums))

    # Test Case 3
    nums = [5,20,66,1314]
    print(maximumCount(nums))