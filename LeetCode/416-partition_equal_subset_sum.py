"""

https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array into two subsets such that
the sum of the elements in both subsets is equal or false otherwise.
 

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

"""

def canPartition(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0:
        return False
    
    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums)):
        nextDp = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDp.add(t + nums[i])
            nextDp.add(t)
        dp = nextDp
    
    return True if target in dp else False

if __name__ == "__main__":
    # Test Case 1
    nums = [1, 5, 11, 5]
    print(canPartition(nums))  # Output is True

    # Test Case 2
    nums = [1, 2, 3, 5]
    print(canPartition(nums))  # Output is False