"""

https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the 
possible permutations. You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

"""

# Recursive
def permute(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return [[]]
    
    perms = permute(nums[1:])

    result = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            result.append(p_copy)
    
    return result

# Iterative
def permuteIterative(nums: list[int]) -> list[list[int]]:
    perms = [[]]

    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(p_copy)
        perms = new_perms
    return perms

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(nums))
    print(permuteIterative(nums))