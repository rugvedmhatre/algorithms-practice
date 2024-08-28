"""

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all 
possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the
solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

"""

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    subset = []
    
    def dfs(i: int) -> None:
        if i >= len(nums):
            result.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
    
    dfs(0)

    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))