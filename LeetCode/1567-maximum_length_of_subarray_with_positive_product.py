"""

https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Given an array of integers nums, find the maximum length of a subarray where the product of all its
elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.


Example 1:
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not 
positive.

Example 3:
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

"""

def getMaxLen(nums: list[int]) -> int:
    result = 0
    pos_len = 0
    neg_len = 0

    for num in nums:
        if num > 0:
            pos_len += 1 
            if neg_len:
                neg_len += 1
        elif num < 0:
            prev_pos_len = pos_len
            if neg_len:
                pos_len = 1 + neg_len
            else:
                pos_len = 0
            neg_len = 1 + prev_pos_len
        else:
            pos_len = 0
            neg_len = 0
    
        result = max(result, pos_len)

    return result

if __name__ == "__main__":
    # Test Case 1
    nums = [1,-2,-3,4]
    print(getMaxLen(nums))

    # Test Case 2
    nums = [0,1,-2,-3,-4]
    print(getMaxLen(nums))

    # Test Case 3
    nums = [-1,-2,-3,0,1]
    print(getMaxLen(nums))